
(function(){
 var p=document.getElementById('prog');
 if(p){var t=function(){var d=document.documentElement,
   h=d.scrollHeight-d.clientHeight;p.style.width=(h>0?(d.scrollTop/h*100):0)+'%';};
  addEventListener('scroll',t,{passive:true});addEventListener('resize',t);t();}

 var NAVH=parseInt(getComputedStyle(document.documentElement).getPropertyValue('--navh'),10)||58;
 var cards=[].slice.call(document.querySelectorAll('.mcard'));
 if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target);}});},{threshold:.15});
  cards.forEach(function(c){io.observe(c);});
  var heads=[].slice.call(document.querySelectorAll('h2[id]'));
  var pills={}; [].forEach.call(document.querySelectorAll('.nav a'),function(a){
    var h=a.getAttribute('href')||''; if(h.charAt(0)==='#') pills[h.slice(1)]=a;});
  if(heads.length&&Object.keys(pills).length){
   var nio=new IntersectionObserver(function(es){es.forEach(function(e){
     if(!e.isIntersecting) return;
     for(var k in pills) pills[k].removeAttribute('aria-current');
     var a=pills[e.target.id]; if(a) a.setAttribute('aria-current','location');
   });},{rootMargin:'-'+NAVH+'px 0px -70% 0px'});
   heads.forEach(function(h){nio.observe(h);});
  }
 }else{cards.forEach(function(c){c.classList.add('on');});}

 var nu=document.querySelector('.nav ul');
 if(nu&&nu.parentNode){
   var edge=function(){nu.parentNode.classList.toggle('at-end',
     nu.scrollLeft+nu.clientWidth>=nu.scrollWidth-2);};
   nu.addEventListener('scroll',edge,{passive:true});addEventListener('resize',edge);edge();
 }

 var live=document.getElementById('cplive');
 [].forEach.call(document.querySelectorAll('.mc-lnk'),function(b){
   var label=b.textContent, timer=null;
   var done=function(){b.textContent='Copied';if(live)live.textContent='Link copied';
     clearTimeout(timer);timer=setTimeout(function(){b.textContent=label;},1500);};
   b.addEventListener('click',function(){
     var u=location.origin+location.pathname+'#'+b.getAttribute('data-a');
     var old=b.parentNode.querySelector('.mc-url'); if(old)old.remove();
     function clip(){
       if(navigator.clipboard&&navigator.clipboard.writeText){
         navigator.clipboard.writeText(u).then(done,function(){fb(u);});
       } else fb(u);
     }
     if(navigator.share){
       navigator.share({url:u}).then(done,function(err){
         if(!err||err.name!=='AbortError')clip();
       });
       return;
     }
     clip();
     function fb(u){
       var i=document.createElement('textarea');
       i.value=u; i.setAttribute('readonly','');
       i.style.cssText='position:fixed;top:0;left:0;width:1px;height:1px;opacity:0;font-size:16px;border:0;padding:0';
       document.body.appendChild(i); i.select();
       try{i.setSelectionRange(0,u.length);}catch(e){}
       var ok=false; try{ok=document.execCommand('copy');}catch(e){}
       i.remove();
       if(ok){done();return;}
       var f=document.createElement('input');
       f.readOnly=true; f.value=u; f.className='mc-url';
       f.setAttribute('aria-label','Link to this game, select and copy');
       b.parentNode.appendChild(f); f.select();
       if(live)live.textContent='Copy the link from the box below';
     }
   });
 });

 if(location.hash){var h0=document.getElementById(location.hash.slice(1));
   if(h0&&h0.classList.contains('mc-row'))h0.classList.add('lit');
   // A deep link fires before fonts and audio players settle, so the browser's
   // first jump lands in the wrong place. Re-aim it until the layout stops moving,
   // and stand down the moment the reader takes over.
   var hTgt=document.getElementById(location.hash.slice(1));
   if(hTgt){
     var userMoved=false,lastY=-1;
     var onWheel=function(){userMoved=true;};
     addEventListener('wheel',onWheel,{passive:true,once:true});
     addEventListener('touchstart',onWheel,{passive:true,once:true});
     addEventListener('keydown',onWheel,{once:true});
     var aim=function(){
       if(userMoved)return;
       var y=Math.round(hTgt.getBoundingClientRect().top);
       if(y===lastY)return; lastY=y;
       hTgt.scrollIntoView({behavior:'auto',block:'start'});
     };
     // Content above the target keeps growing for several seconds as fonts land and
     // the audio players report their durations, and Chrome's scroll anchoring then
     // slides the target back out of view. Keep re-aiming until it stops moving.
     var tries=0,iv=setInterval(function(){aim();if(++tries>70||userMoved)clearInterval(iv);},120);
     addEventListener('load',aim);
     if(document.fonts&&document.fonts.ready)document.fonts.ready.then(aim);
     [].forEach.call(document.querySelectorAll('audio'),function(a){
       a.addEventListener('loadedmetadata',function(){lastY=-1;aim();});
       a.addEventListener('canplay',function(){lastY=-1;aim();});
     });
   }
 }

 var j=document.getElementById('jump');
 if(j){
   var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
   j.addEventListener('change',function(){
     var el=j.value&&document.getElementById(j.value); if(!el)return;
     el.scrollIntoView({behavior:rm?'auto':'smooth',block:'start'});
     el.setAttribute('tabindex','-1');
     try{el.focus({preventScroll:true});}catch(e){}
     [].forEach.call(document.querySelectorAll('.lit'),function(x){x.classList.remove('lit');});
     el.classList.add('lit');
     if(history.replaceState)history.replaceState(null,'','#'+j.value);
     j.selectedIndex=0;
   });
 }

 var PLAY='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M8 5.2v13.6a1 1 0 0 0 1.53.85l10.6-6.8a1 1 0 0 0 0-1.7L9.53 4.35A1 1 0 0 0 8 5.2z"/></svg>';
 var PAUS='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 4h4v16H7zM13 4h4v16h-4z"/></svg>';
 var all=[].slice.call(document.querySelectorAll('.au'));
 var fmt=function(s){s=Math.max(0,Math.round(s||0));
   return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2);};
 all.forEach(function(box){
   var a=box.querySelector('audio'); if(!a) return;
   var mid=box.querySelector('.au-m'); if(!mid) return;
   a.removeAttribute('controls'); a.classList.add('sr');
   var ttl=box.querySelector('.au-t');
   var name=box.getAttribute('data-label')||(ttl?ttl.textContent:'audio');
   var btn=document.createElement('button');
   btn.type='button'; btn.className='au-btn'; btn.innerHTML=PLAY;
   btn.setAttribute('aria-label','Play: '+name);
   var bar=document.createElement('div'); bar.className='au-bar';
   var fil=document.createElement('i'); bar.appendChild(fil);
   var tm=document.createElement('span'); tm.className='au-time'; tm.textContent='--:--';
   mid.appendChild(bar);
   box.insertBefore(btn,box.firstChild); box.appendChild(tm);
   bar.setAttribute('role','slider'); bar.setAttribute('tabindex','0');
   bar.setAttribute('aria-label','Seek: '+name);
   bar.setAttribute('aria-valuemin','0'); bar.setAttribute('aria-valuemax','100');
   bar.setAttribute('aria-valuenow','0');

   var failed=false;
   var fail=function(){
     if(failed)return; failed=true;
     box.classList.add('dead');
     btn.disabled=true; btn.setAttribute('aria-label','Audio unavailable');
     bar.style.display='none'; tm.style.minWidth='0'; tm.textContent='Unavailable';
   };
   a.addEventListener('error',fail);

   btn.addEventListener('click',function(){
     if(a.paused){
       if(!a.currentTime){try{var v=+sessionStorage.getItem('wb:'+a.src);
         if(v>3&&(!a.duration||v<a.duration-3))a.currentTime=v;}catch(e){}}
       all.forEach(function(o){var x=o.querySelector('audio'); if(x&&x!==a)x.pause();});
       var pr=a.play();
       if(pr&&pr.catch)pr.catch(function(err){
         if(err&&(err.name==='AbortError'||err.name==='NotAllowedError'))return;
         fail();
       });
     } else a.pause();
   });
   var seek=function(f){if(a.duration)a.currentTime=Math.min(a.duration,Math.max(0,f*a.duration));};
   bar.addEventListener('click',function(e){var r=bar.getBoundingClientRect();
     seek((e.clientX-r.left)/r.width);});
   bar.addEventListener('keydown',function(e){
     var d=a.duration||0; if(!d)return; var k=e.key;
     if(k==='ArrowRight'||k==='ArrowUp')a.currentTime=Math.min(d,a.currentTime+5);
     else if(k==='ArrowLeft'||k==='ArrowDown')a.currentTime=Math.max(0,a.currentTime-5);
     else if(k==='Home')a.currentTime=0; else if(k==='End')a.currentTime=d; else return;
     e.preventDefault();
   });
   a.addEventListener('play',function(){btn.innerHTML=PAUS;btn.setAttribute('aria-label','Pause: '+name);});
   a.addEventListener('pause',function(){btn.innerHTML=PLAY;btn.setAttribute('aria-label','Play: '+name);});
   a.addEventListener('waiting',function(){btn.style.opacity='.55';});
   a.addEventListener('playing',function(){btn.style.opacity='';});
   a.addEventListener('loadedmetadata',function(){tm.textContent=fmt(a.duration);});
   var lastSave=0;
   var save=function(){try{
     if(a.currentTime>3&&a.duration&&a.currentTime<a.duration-3)
       sessionStorage.setItem('wb:'+a.src,a.currentTime);
     else sessionStorage.removeItem('wb:'+a.src);
   }catch(e){}};
   a.addEventListener('pause',save);
   addEventListener('pagehide',save);
   a.addEventListener('timeupdate',function(){
     if(!a.duration) return;
     var pct=a.currentTime/a.duration*100;
     fil.style.width=pct+'%';
     bar.setAttribute('aria-valuenow',Math.round(pct));
     bar.setAttribute('aria-valuetext',fmt(a.currentTime)+' of '+fmt(a.duration));
     tm.textContent=fmt(a.duration-a.currentTime);
     if(a.currentTime-lastSave>4){lastSave=a.currentTime;save();}
   });
   a.addEventListener('ended',function(){fil.style.width='0%';tm.textContent=fmt(a.duration);
     try{sessionStorage.removeItem('wb:'+a.src);}catch(e){}});
 });
})();
