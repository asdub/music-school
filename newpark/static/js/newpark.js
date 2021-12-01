// Music Section display pathway menu when in view.
const buttons = document.querySelectorAll('.pathway');
const overlay = document.querySelector('.music-hero-overlay');
const divs = document.querySelectorAll('.path-container');
const inners = document.querySelectorAll('a.btn-path-inner');

const head = document.getElementsByTagName('head')[0];

let space = getComputedStyle(document.body).getPropertyValue('--pathway-space');
let style = document.createElement('style');
let styles = [];
let keyframes;

const config = {
    rootMargin: '0px',
    threshold: [0, 0.25, 0.75, 1]
  };

observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.intersectionRatio > 0.5) {
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
          console.log(i)
          inner.style.animation = 'inner'+ i +' 0.5s'
          inner.style.animationFillMode = 'forwards'
        });
        styles.forEach((k) => {
          style.insertAdjacentHTML('afterBegin', k);
        });
    } else {
        overlay.classList.remove('music-hero-active');
        divs.forEach(div => {
          
        });
    }
  });
  head.appendChild(style);
}, config);

buttons.forEach(button => {
  observer.observe(button);
});