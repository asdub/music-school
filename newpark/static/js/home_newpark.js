// Music Section display pathway menu when in view.
window.addEventListener('load', (event) => {
  const buttons = document.querySelectorAll('.pathway');
  const overlay = document.querySelector('.music-hero-overlay');
  const divs = document.querySelectorAll('.path-container');
  const inners = document.querySelectorAll('a.btn-path-inner');

  const head = document.getElementsByTagName('head')[0];
  const mediaQuery = window.matchMedia('(min-width: 768px)')

  let space = getComputedStyle(document.body).getPropertyValue('--pathway-space');
  let style = document.createElement('style');
  let slineActive;
  let position;
  let styles = [];
  let keyframes;

  const config = {
      rootMargin: '0px',
      threshold: [0, 0.25, 0.75, 1]
    };

  if (mediaQuery.matches) {
    slineActive = 1
    startPosition = 'right'
    endPostion = 'left'
  } else {
    slineActive = 0
    startPosition = 'bottom'
    endPostion = 'top'
  };

  // Progression Line
  line = new LeaderLine(document.getElementById('a1'),  document.getElementById('d'));
  line.setOptions({
    startPlug: 'behind',
    endPlug: 'behind',
    color: 'white',
    startSocket: startPosition,
    endSocket: endPostion,
  });
  if (slineActive == 1) {
    bline = new LeaderLine(document.getElementById('a2'),  document.getElementById('b'));
    bline.setOptions({
      startPlug: 'behind',
      endPlug: 'behind',
      color: 'white',
      path: 'grid',
    });

    sline = new LeaderLine(document.getElementById('a3'),  document.getElementById('c'));
    sline.setOptions({
      startPlug: 'behind',
      endPlug: 'behind',
      color: 'white',
    });
  }

  function lineupdate() {
    timer = requestAnimationFrame(lineupdate);
    line.position();
    if (slineActive == 1) {
      bline.position();
      sline.position();
    }
  }

  // Animations and Triggers
  observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.intersectionRatio > 0.65) {
          overlay.classList.add('music-hero-active');
          divs.forEach((div, i) => {
            keyframes = 
              `@keyframes move`+ i +` {
              from { transform: translateX(0px); }
              to { transform: translateX(`+ i * space +`px);}}`;
              styles.push(keyframes)
            setTimeout(function(){
              div.style.animation = 'move'+ i +' 0.5s'
              div.style.animationFillMode = 'forwards'
            }, i * 100);
          });
          inners.forEach((inner, i) => {
            innerframe = 
              `@keyframes inner`+ i +` {
              from { transform: translateX(0px); }
              to { transform: translateX(`+ (i * 0.4) * space +`px);}}`;
            styles.push(innerframe)
            inner.style.animation = 'inner'+ i +' 0.5s'
            inner.style.animationFillMode = 'forwards'
          });
          styles.forEach((k) => {
            style.insertAdjacentHTML('afterBegin', k);
          });
          setTimeout(function(){
            line.show('draw', {duration: 3000});
            if (slineActive == 1) {
              bline.show('draw', {duration: 3100});
              sline.show('draw', {duration: 3200});
            }
          }, );
      } else {
          line.hide('fade');
          if (slineActive == 1) {
            bline.hide('fade');
            sline.hide('fade');
          }
          overlay.classList.remove('music-hero-active');
          style.innerHTML = '';
      }
    });
    head.appendChild(style);
    lineupdate()
  }, config);

  buttons.forEach(button => {
    observer.observe(button);
  });
});