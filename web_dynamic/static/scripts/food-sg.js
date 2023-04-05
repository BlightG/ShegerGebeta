$(function () {
    let search_bttn = document.querySelector('.search_bttn');
    let search_field = document.querySelector('.search_bar');
    let location_bttn = document.querySelector('button.location');
    let home_bttn = document.querySelector('button.home');
    let food_bttn = document.querySelector('button.foods');
  
    search_bttn.addEventListener('click',  () => {
      let value = search_field.value;
      if (value) {
        window.open('http://172.26.250.210:5000/place/name/' + value, '_self');
      };
    })
  
    location_bttn.addEventListener('click', () => {
      window.open('http://172.26.250.210:5000/place', '_self');
    });
  
    food_bttn.addEventListener('click', () => {
      window.open('http://172.26.250.210:5000/', '_self')
    });
  
    home_bttn.addEventListener('click', () => {
      window.open('http://172.26.250.210:5000/', '_self')
    });
  
    location_bttn
  })