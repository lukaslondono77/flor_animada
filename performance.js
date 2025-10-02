// Performance monitoring for Flor Animada
class PerformanceMonitor {
    constructor() {
        this.metrics = {};
        this.startTime = performance.now();
    }

    // Track page load time
    trackPageLoad() {
        window.addEventListener('load', () => {
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            this.metrics.pageLoadTime = loadTime;
            console.log(`📊 Page loaded in ${loadTime}ms`);
            
            // Send to analytics if available
            if (typeof gtag !== 'undefined') {
                gtag('event', 'page_load', {
                    'value': loadTime,
                    'event_category': 'performance'
                });
            }
        });
    }

    // Track image load times
    trackImageLoad(imageName) {
        const startTime = performance.now();
        const img = new Image();
        
        img.onload = () => {
            const loadTime = performance.now() - startTime;
            this.metrics[`image_${imageName}`] = loadTime;
            console.log(`🖼️ ${imageName} loaded in ${loadTime.toFixed(2)}ms`);
        };
        
        img.src = `static/images/${imageName}`;
    }

    // Track user interactions
    trackInteraction(action) {
        const timestamp = Date.now();
        console.log(`👆 User interaction: ${action} at ${timestamp}`);
        
        if (!this.metrics.interactions) {
            this.metrics.interactions = [];
        }
        this.metrics.interactions.push({ action, timestamp });
    }

    // Get performance summary
    getSummary() {
        const totalTime = performance.now() - this.startTime;
        return {
            ...this.metrics,
            totalSessionTime: totalTime,
            timestamp: Date.now()
        };
    }
}

// Initialize performance monitoring
const perfMonitor = new PerformanceMonitor();
perfMonitor.trackPageLoad();

// Track form submissions
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('mainForm');
    if (form) {
        form.addEventListener('submit', () => {
            perfMonitor.trackInteraction('form_submit');
        });
    }

    // Track reset button clicks
    const resetBtn = document.querySelector('.reset-btn');
    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            perfMonitor.trackInteraction('reset_click');
        });
    }
});

// Export for use in other scripts
window.PerformanceMonitor = PerformanceMonitor;
window.perfMonitor = perfMonitor;
