document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Animation
    const reveals = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const elementVisible = 100;

        reveals.forEach((reveal) => {
            const elementTop = reveal.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                reveal.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger once on load

    // Floating Hearts Background Animation
    const heartsBg = document.getElementById('hearts-bg');
    const createHeart = () => {
        if (!heartsBg) return;
        const heart = document.createElement('div');
        heart.classList.add('heart-shape');
        
        // Randomize size, position and animation duration
        const size = Math.random() * 20 + 10; // 10px to 30px
        const left = Math.random() * 100; // 0% to 100%
        const duration = Math.random() * 10 + 15; // 15s to 25s
        const delay = Math.random() * 5; // 0s to 5s
        
        heart.innerHTML = '<i class="fa-solid fa-heart"></i>';
        heart.style.fontSize = `${size}px`;
        heart.style.left = `${left}%`;
        heart.style.animationDuration = `${duration}s`;
        heart.style.animationDelay = `${delay}s`;
        
        heartsBg.appendChild(heart);
        
        // Remove heart after animation to prevent memory leak
        setTimeout(() => {
            heart.remove();
        }, (duration + delay) * 1000);
    };

    // Create initial hearts
    for (let i = 0; i < 15; i++) {
        setTimeout(createHeart, Math.random() * 3000);
    }

    // Continue creating hearts
    setInterval(createHeart, 2000);

    // Smooth scroll down button
    const scrollDownBtn = document.querySelector('.scroll-down');
    if (scrollDownBtn) {
        scrollDownBtn.addEventListener('click', () => {
            window.scrollTo({
                top: window.innerHeight,
                behavior: 'smooth'
            });
        });
    }

    // Lightbox Logic
    const lightbox = document.getElementById('lightbox');
    if (lightbox) {
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxClose = document.getElementById('lightbox-close');
        
        // Select gallery images AND details cards images
        const clickableImages = document.querySelectorAll('.masonry-item img, .card-img img');

        clickableImages.forEach(img => {
            img.addEventListener('click', () => {
                lightboxImg.src = img.src;
                lightbox.classList.add('active');
                document.body.style.overflow = 'hidden'; // prevent scrolling
            });
        });

        const closeLightbox = () => {
            lightbox.classList.remove('active');
            document.body.style.overflow = 'auto';
        };

        lightboxClose.addEventListener('click', closeLightbox);

        lightbox.addEventListener('click', (e) => {
            if (e.target !== lightboxImg) {
                closeLightbox();
            }
        });
    }

    // Audio Logic
    const bgMusic = document.getElementById('bg-music');
    const musicToggle = document.getElementById('music-toggle');

    if (bgMusic && musicToggle) {
        let isPlaying = false;
        musicToggle.addEventListener('click', () => {
            if (isPlaying) {
                bgMusic.pause();
                musicToggle.classList.remove('playing');
                musicToggle.innerHTML = '<i class="fa-solid fa-music"></i>';
            } else {
                bgMusic.play().catch(e => console.log('Audio bloqueado pelo navegador', e));
                musicToggle.classList.add('playing');
                musicToggle.innerHTML = '<i class="fa-solid fa-pause"></i>';
            }
            isPlaying = !isPlaying;
        });
    }

    // Smooth background transitions on scroll
    const sections = document.querySelectorAll('.gallery-section, .details-section, .love-letter-section');
    // Color palette that alternates smoothly
    const colors = [
        '#faf3f5', // Default pink
        '#ffffff', // Pure white
        '#fdf4f6', // Slightly warmer pink
        '#ffffff', 
        '#f5e6e8', // Rose gold
        '#ffffff',
        '#fcf0f2'
    ];

    const observerOptions = {
        root: null,
        threshold: 0.15, // Trigger when 15% of section is visible
        rootMargin: "-10% 0px -10% 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionIndex = Array.from(sections).indexOf(entry.target);
                if (sectionIndex !== -1) {
                    const nextColor = colors[sectionIndex % colors.length];
                    if (entry.target.classList.contains('details-section')) {
                        document.body.style.backgroundColor = '#c4294b';
                    } else {
                        document.body.style.backgroundColor = nextColor;
                    }
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => observer.observe(section));
});
