// ====== 龙奕学院 Theme Toggle v1.0 ======
// 全局日间/夜间模式切换，支持所有8个学院主题
(function(){
  const KEY = 'longyi-theme';
  const MODES = ['light','dark'];
  
  function get(){ try{return localStorage.getItem(KEY)||'light';}catch(e){return 'light';} }
  function set(m){
    try{localStorage.setItem(KEY,m);}catch(e){}
    apply(m);
  }
  
  function apply(mode){
    const root = document.documentElement;
    // Remove both, then add current
    root.classList.remove('theme-light','theme-dark');
    root.classList.add('theme-'+mode);
    
    // Update toggle button if exists
    const btn = document.getElementById('themeToggle');
    if(btn){
      btn.innerHTML = mode==='dark'
        ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
        : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>';
      btn.title = mode==='dark'?'切换到日间模式':'切换到夜间模式';
    }
    
    // Dispatch event for other components
    window.dispatchEvent(new CustomEvent('themeChange',{detail:{mode}}));
    
    // Update meta theme-color
    let meta = document.querySelector('meta[name=theme-color]');
    if(!meta){
      meta = document.createElement('meta'); meta.name='theme-color';
      document.head.appendChild(meta);
    }
    meta.content = mode==='dark'?'#0a0a1a':'#fafaff';
    
    // Animate transition
    document.body.style.transition = 'background-color 0.4s ease, color 0.3s ease';
    setTimeout(()=>{document.body.style.transition='';},500);
  }
  
  // Init
  apply(get());
  
  // Toggle button handler
  document.addEventListener('click',function(e){
    if(e.target.closest('#themeToggle')){
      set(get()==='dark'?'light':'dark');
    }
  });
  
  // Keyboard shortcut: Ctrl/Cmd + Shift + D
  document.addEventListener('keydown',function(e){
    if((e.ctrlKey||e.metaKey) && e.shiftKey && e.key.toLowerCase()==='d'){
      e.preventDefault();
      set(get()==='dark'?'light':'dark');
    }
  });
  
  // Expose globally
  window.LongYiTheme={get,set,apply};
})();
