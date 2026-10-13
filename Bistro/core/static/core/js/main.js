// Scroll-in animations for every element that has a data-aos attribute
AOS.init({
    duration: 800,
    easing: 'ease-out-cubic',
    once: true,
    offset: 60,
});

// Shadow under the navbar once the page has been scrolled
const header = document.querySelector('header');

function updateHeader() {
    header.dataset.scrolled = window.scrollY > 10;
}

window.addEventListener('scroll', updateHeader, { passive: true });
updateHeader();

// Favourites and cart are remembered in the browser, so they survive a reload
function load(key) {
    try {
        return JSON.parse(localStorage.getItem(key)) || [];
    } catch {
        return [];
    }
}

function save(key, list) {
    try {
        localStorage.setItem(key, JSON.stringify(list));
    } catch {
        // Storage is blocked (for example in a private window): the buttons
        // still work, they are just forgotten when the page reloads
    }
}

// Adds the item when it is missing, removes it when it is there.
// Returns true when the item ends up in the list.
function toggle(list, item) {
    const index = list.indexOf(item);
    if (index === -1) {
        list.push(item);
        return true;
    }
    list.splice(index, 1);
    return false;
}

function pop(element) {
    element.animate(
        [{ transform: 'scale(1)' }, { transform: 'scale(1.35)' }, { transform: 'scale(1)' }],
        { duration: 350, easing: 'ease-out' }
    );
}

const toast = document.getElementById('toast');
let toastTimer;

function showToast(message) {
    toast.textContent = message;
    toast.dataset.visible = 'true';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
        toast.dataset.visible = 'false';
    }, 2200);
}

function setPressed(button, pressed, labels) {
    button.setAttribute('aria-pressed', pressed);
    button.setAttribute('aria-label', pressed ? labels.on : labels.off);
}

const cards = [...document.querySelectorAll('[data-dish]')];
const dishNames = cards.map((card) => card.dataset.dish);
const favourites = load('bistro-favourites').filter((name) => dishNames.includes(name));
const cart = load('bistro-cart').filter((name) => dishNames.includes(name));

const cartLink = document.getElementById('cart-link');
const cartCount = document.getElementById('cart-count');

function updateCartCount() {
    cartCount.textContent = cart.length;
    cartLink.setAttribute('aria-label', `Cart, ${cart.length} item${cart.length === 1 ? '' : 's'}`);
}

cards.forEach((card) => {
    const name = card.dataset.dish;
    const heartButton = card.querySelector('[data-action="favourite"]');
    const cartButton = card.querySelector('[data-action="cart"]');
    const heartLabels = { off: `Add ${name} to favourites`, on: `Remove ${name} from favourites` };
    const cartLabels = { off: `Add ${name} to cart`, on: `Remove ${name} from cart` };

    setPressed(heartButton, favourites.includes(name), heartLabels);
    setPressed(cartButton, cart.includes(name), cartLabels);

    heartButton.addEventListener('click', () => {
        const added = toggle(favourites, name);
        save('bistro-favourites', favourites);
        setPressed(heartButton, added, heartLabels);
        pop(heartButton);
        showToast(added ? `${name} added to favourites` : `${name} removed from favourites`);
    });

    cartButton.addEventListener('click', () => {
        const added = toggle(cart, name);
        save('bistro-cart', cart);
        setPressed(cartButton, added, cartLabels);
        updateCartCount();
        pop(cartButton);
        pop(cartCount);
        showToast(added ? `${name} added to cart` : `${name} removed from cart`);
    });
});

updateCartCount();

// Motion that follows the scroll position, done with GSAP's ScrollTrigger plugin
gsap.registerPlugin(ScrollTrigger);

// Parallax: each story photo is taller than its frame and drifts inside it
// while the frame crosses the screen
gsap.utils.toArray('[data-parallax]').forEach((photo) => {
    gsap.fromTo(photo, { yPercent: -11 }, {
        yPercent: 11,
        ease: 'none',
        scrollTrigger: { trigger: photo.parentElement, start: 'top bottom', end: 'bottom top', scrub: 0.6 },
    });
});

// Depth: anything with data-drift moves at its own speed while its chapter
// (or its section) crosses the screen. The value is the distance in pixels;
// a negative value lags behind the page.
gsap.utils.toArray('[data-drift]').forEach((layer) => {
    const distance = Number(layer.dataset.drift);
    gsap.fromTo(layer, { y: distance }, {
        y: -distance,
        ease: 'none',
        scrollTrigger: { trigger: layer.closest('[data-chapter], section'), start: 'top bottom', end: 'bottom top', scrub: 0.6 },
    });
});

// The story in the About section
const story = document.getElementById('story');

if (story) {
    // The red line draws itself down the page as the chapters go by
    gsap.fromTo('#story-line', { scaleY: 0 }, {
        scaleY: 1,
        ease: 'none',
        scrollTrigger: { trigger: story, start: 'top 55%', end: 'bottom 55%', scrub: true },
    });

    // A chapter's dot lights up when the line reaches it
    gsap.utils.toArray('[data-chapter]').forEach((chapter) => {
        ScrollTrigger.create({
            trigger: chapter.querySelector('[data-dot]'),
            start: 'center 55%',
            onEnter: () => { chapter.dataset.active = 'true'; },
            onLeaveBack: () => { chapter.dataset.active = 'false'; },
        });
    });
}

// Contact form: it is not connected to Django yet, so stop the page reload
// and say so instead of pretending the message was sent
const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        showToast('Form preview only. Messages are not sent yet.');
    });
}
