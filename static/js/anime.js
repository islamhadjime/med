

let hbtn = document.querySelector('.header__row-mobile');
let header__wrappers = document.querySelector('.header__wrappers')
const root = document.querySelector(":root")

// https://codepen.io/noirsociety/pen/ZEwLGXB
document.querySelector("#clickModal").addEventListener('click', () => {
  document.body.classList.add('activaModal')
  document.querySelector('#closeModal').addEventListener('click', () => {
    document.body.classList.remove('activaModal')
  })
})








function queryElement(el, state) {
  document.querySelector(el).style.display = state
}

hbtn.addEventListener('click', function (e) {
  header__wrappers.classList.toggle('mobil_app')
  if (header__wrappers.classList.contains('mobil_app')) {
    queryElement('.end_clock', 'none');
    queryElement('.click_look', 'block');
  } else {
    queryElement('.end_clock', 'block');
    queryElement('.click_look', 'none');
  }

})

if (localStorage.theme == 1) {
  document.body.classList.add('dark')
  document.querySelector('.ball').style.transform = 'translateY(24px)'
}


document.querySelector('#chk').addEventListener('click', () => {
  if (localStorage.theme == null || localStorage.theme == 0) {
    document.body.classList.add('dark')
    document.querySelector('.ball').style.transform = 'translateY(24px)'
    localStorage.theme = 1
  } else if (localStorage.theme == 1) {
    document.body.classList.remove('dark')
    document.querySelector('.ball').style.transform = 'translateY(0px)'
    localStorage.theme = 0
  }
});




window.addEventListener('scroll', function () {
  if (this.pageYOffset <= 1370) {
    animStart(document.querySelector('.stats_round_1'), 15)
    animStart(document.querySelector('.stats_round_2'), 5623)
    animStart(document.querySelector('.stats_round_3'), 20)
    return true
  }
});



function animStart(el, con) {
  return anime({
    targets: el,
    innerHTML: [0, con],
    easing: 'linear',
    round: 10 // Will round the animated value to 1 decimal
  });
}

