//Toggle menu hamburger
const menuIcon = document.querySelector('.menu-icon');
const menu = document.querySelector('.menu');

menuIcon.addEventListener('click', function(){
    this.classList.toggle('active');
    menu.classList.toggle('active');

    if(menu.classList.contains('active')){
        const headerHight = document.querySelector('header').offsetHeight;
        menu.style.top = headerHight + 'px';

    }else{
        menu.style.top = '';
    }
});

const carousels = document.querySelectorAll('.car-carousel');

carousels.forEach(carousel => {
    const prevButton = carousel.parentElement.querySelector('.carousel-prev');
    const nextButton = carousel.parentElement.querySelector('.carousel-next');
    
    const items = carousel.querySelectorAll('.car-card');

    let currentIndex = 0;

    const updateCarousel = () => {
        items.forEach((item, index) => {
            if(index === currentIndex) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    };

    nextButton.addEventListener('click', () =>{
        if(currentIndex < items.length -1) {
            currentIndex++;
        } else{
            currentIndex = 0;
        }

        updateCarousel();
    });

    prevButton.addEventListener('click', () =>{
        if(currentIndex > 0){
            currentIndex--;
        } else{
            currentIndex = items.length -1;
        }

        updateCarousel();
    });

    updateCarousel();
})