// activities_detail.js - Mobile optimized auto-scroller
document.addEventListener("DOMContentLoaded", () => {
  console.log("Mobile-optimized auto-scroller initializing...");
  
  // Check if mobile device
  const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
  const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
  
  // Get elements
  const templateContainer = document.getElementById('cards-track');
  const viewport = document.getElementById('cardsViewport');
  const touchIndicator = document.querySelector('.touch-indicator');
  
  if (!templateContainer || !viewport) {
    console.error('Required elements not found');
    return;
  }
  
  // Collect existing images from the template
  const existingCards = templateContainer.querySelectorAll('.mini-card');
  const sourceItems = [];
  
  if (existingCards.length > 0) {
    existingCards.forEach(card => {
      const img = card.querySelector('img');
      if (img) {
        sourceItems.push({
          src: img.getAttribute('src'),
          alt: img.getAttribute('alt') || ''
        });
      }
    });
  }
  
  // If no images found, use fallback
  if (sourceItems.length === 0) {
    console.warn('No images found, using fallback');
    sourceItems.push(
      { src: '/static/image/softplay.jpg', alt: 'Soft Play' },
      { src: '/static/image/toddlers.jpeg', alt: 'Toddlers' },
      { src: '/static/image/softplay.jpg', alt: 'Soft Play 2' },
      { src: '/static/image/softplay.jpg', alt: 'Soft Play 3' }
    );
  }
  
  // Clear container
  templateContainer.innerHTML = '';
  templateContainer.style.overflow = 'hidden';
  templateContainer.style.position = 'relative';
  
  // Create scroll inner container
  const scrollInner = document.createElement('div');
  scrollInner.className = 'scroll-inner';
  scrollInner.style.willChange = 'transform';
  scrollInner.style.transform = 'translate3d(0,0,0)';
  scrollInner.style.transition = 'transform 0.1s ease-out'; // Smoother on mobile
  templateContainer.appendChild(scrollInner);
  
  // Function to add a set of cards
  function appendOneSet() {
    sourceItems.forEach(item => {
      const card = document.createElement('div');
      card.className = 'mini-card';
      
      const img = document.createElement('img');
      img.src = item.src;
      img.alt = item.alt;
      img.loading = 'lazy';
      img.decoding = 'async'; // Better performance
      
      // Handle image errors
      img.onerror = () => {
        const placeholder = document.createElement('div');
        placeholder.className = 'img-placeholder';
        placeholder.textContent = item.alt || 'Image';
        card.innerHTML = '';
        card.appendChild(placeholder);
      };
      
      card.appendChild(img);
      scrollInner.appendChild(card);
    });
  }
  
  // Add two sets for seamless scrolling
  appendOneSet();
  appendOneSet();
  
  // Calculate the height of one set
  function computeSetHeight() {
    const cards = scrollInner.querySelectorAll('.mini-card');
    const perSet = sourceItems.length;
    
    if (cards.length < perSet) return 0;
    
    let totalHeight = 0;
    
    // Use first card height times number of cards (faster than measuring all)
    if (cards[0]) {
      const firstCardHeight = cards[0].getBoundingClientRect().height;
      totalHeight = firstCardHeight * perSet;
    }
    
    // Add gaps
    const computedStyle = window.getComputedStyle(scrollInner);
    const gapValue = computedStyle.gap || computedStyle.rowGap;
    if (gapValue && gapValue !== 'normal') {
      const gap = parseFloat(gapValue) || 0;
      totalHeight += gap * Math.max(0, perSet - 1);
    }
    
    return Math.round(totalHeight);
  }
  
  // Mobile-optimized scrolling system
  async function startScroller() {
    // Wait a bit for images to load (but don't block)
    setTimeout(() => {
      initScrolling();
    }, 300);
  }
  
  function initScrolling() {
    let setHeight = computeSetHeight();
    if (setHeight === 0) {
      // Use viewport height as fallback
      setHeight = Math.max(1, viewport.clientHeight * 2.5);
    }
    
    // Adjust speed based on device
    const PIXELS_PER_SECOND = isMobile ? 40 : 50; // Slower on mobile
    
    let offset = 0;
    let lastTime = null;
    let paused = false;
    let touchStartY = 0;
    let touchStartOffset = 0;
    let isTouching = false;
    let velocity = 0;
    let lastOffset = 0;
    let lastDeltaTime = 0;
    
    // Show touch indicator briefly on mobile
    if (isTouchDevice && touchIndicator) {
      setTimeout(() => {
        touchIndicator.style.opacity = '1';
        setTimeout(() => {
          touchIndicator.style.opacity = '0';
        }, 2000);
      }, 1000);
    }
    
    // Touch events for mobile
    if (isTouchDevice) {
      viewport.addEventListener('touchstart', (e) => {
        e.preventDefault();
        isTouching = true;
        paused = true;
        touchStartY = e.touches[0].clientY;
        touchStartOffset = offset;
        velocity = 0;
        lastOffset = offset;
        lastDeltaTime = Date.now();
        
        viewport.style.cursor = 'grabbing';
      });
      
      viewport.addEventListener('touchmove', (e) => {
        if (!isTouching) return;
        e.preventDefault();
        
        const touchY = e.touches[0].clientY;
        const deltaY = touchY - touchStartY;
        
        // Calculate velocity for momentum scrolling
        const currentTime = Date.now();
        const deltaTime = currentTime - lastDeltaTime;
        if (deltaTime > 0) {
          velocity = (offset - lastOffset) / deltaTime;
          lastOffset = offset;
          lastDeltaTime = currentTime;
        }
        
        offset = touchStartOffset - deltaY;
        
        // Bounce effect at boundaries
        if (offset < 0) {
          offset = offset * 0.3; // Elastic bounce
        } else if (offset > setHeight) {
          offset = setHeight + (offset - setHeight) * 0.3;
        }
        
        scrollInner.style.transform = `translate3d(0, -${offset}px, 0)`;
      });
      
      viewport.addEventListener('touchend', () => {
        isTouching = false;
        
        // Apply momentum
        if (Math.abs(velocity) > 0.5) {
          const momentum = velocity * 100;
          offset += momentum;
          
          // Clamp to boundaries
          if (offset < 0) offset = 0;
          if (offset > setHeight) offset = setHeight;
          
          // Smooth transition for momentum
          scrollInner.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
          scrollInner.style.transform = `translate3d(0, -${offset}px, 0)`;
          
          setTimeout(() => {
            scrollInner.style.transition = 'transform 0.1s ease-out';
          }, 300);
        }
        
        // Resume auto-scroll after delay on mobile
        setTimeout(() => {
          paused = false;
          viewport.style.cursor = 'pointer';
        }, 1500);
      });
    }
    
    // Mouse events for desktop
    viewport.addEventListener('mouseenter', () => {
      if (!isTouching) {
        paused = true;
        viewport.style.cursor = 'grab';
      }
    });
    
    viewport.addEventListener('mouseleave', () => {
      if (!isTouching) {
        paused = false;
        viewport.style.cursor = 'pointer';
      }
    });
    
    viewport.addEventListener('mousedown', () => {
      if (!isTouchDevice) {
        viewport.style.cursor = 'grabbing';
      }
    });
    
    viewport.addEventListener('mouseup', () => {
      if (!isTouchDevice) {
        viewport.style.cursor = 'grab';
      }
    });
    
    // Click to pause/unpause (for desktop)
    viewport.addEventListener('click', (e) => {
      if (!isTouchDevice) {
        e.preventDefault();
        paused = !paused;
        viewport.style.cursor = paused ? 'grab' : 'pointer';
      }
    });
    
    // Animation loop
    function animate(currentTime) {
      if (!lastTime) lastTime = currentTime;
      
      const deltaTime = (currentTime - lastTime) / 1000;
      lastTime = currentTime;
      
      // Cap delta time for consistent scrolling
      const maxDelta = isMobile ? 0.1 : 0.05; // More lenient on mobile
      const safeDelta = Math.min(deltaTime, maxDelta);
      
      if (!paused && !isTouching) {
        offset += PIXELS_PER_SECOND * safeDelta;
        
        // Seamless loop
        if (offset >= setHeight) {
          offset = offset % setHeight;
        }
        
        scrollInner.style.transform = `translate3d(0, -${offset}px, 0)`;
      }
      
      requestAnimationFrame(animate);
    }
    
    requestAnimationFrame(animate);
    
    // Optimized resize handler for mobile
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        const newSetHeight = computeSetHeight();
        if (newSetHeight > 0) {
          // Maintain relative position
          const ratio = offset / setHeight;
          setHeight = newSetHeight;
          offset = ratio * setHeight;
        }
      }, 250);
    });
    
    // Handle visibility change (pause when tab is not active)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        paused = true;
      } else {
        // Resume after a short delay
        setTimeout(() => {
          paused = false;
        }, 500);
      }
    });
    
    // Prevent context menu on images
    viewport.addEventListener('contextmenu', (e) => {
      if (e.target.tagName === 'IMG') {
        e.preventDefault();
      }
    });
  }
  
  // Start the scroller
  startScroller();
});