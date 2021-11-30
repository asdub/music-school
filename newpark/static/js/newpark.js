// Music Section display pathway menu when in view.
const buttons = document.querySelectorAll('.pathway');
const overlay = document.querySelector('.music-hero-overlay');
const divs = document.querySelectorAll('.path-container');

const head = document.getElementsByTagName('head')[0];

let style = document.createElement('STYLE');
let keyframes

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
            to { transform: translateX(`+ i * 10 +`px);}}`;
            console.log(keyframes)
          setTimeout(function(){
            div.style.animation = 'move'+ i +' 0.5s'
            div.style.animationFillMode = 'forwards'
            style.innerHTML = keyframes;
          }, i * 100);
        });
    } else {
        overlay.classList.remove('music-hero-active');
        divs.forEach(div => {
          
        });
    }
  });
  head.appendChild(style);
  console.log(style);
}, config);

buttons.forEach(button => {
  observer.observe(button);
});