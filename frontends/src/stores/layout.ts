import { ref, onMounted, onUnmounted } from "vue";
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

export class LayoutHelpers {

    static carouselItemsToShow(): any {
      let itemsToShow = ref(3);
  
      // Responsive breakpoints
      const breakpoints = useBreakpoints(breakpointsTailwind)
      function resolveItemsToShow() {
        // breakpoints on md
        if (breakpoints.isGreater('md')) {
          itemsToShow.value = 5
        } else {
          itemsToShow.value = 3
        }
    }
  
      // Listen to resize event
      onMounted(() => {
        window.addEventListener("resize", resolveItemsToShow);
        resolveItemsToShow();
      });
      onUnmounted(() => {
        window.removeEventListener("resize", resolveItemsToShow);
      });
  
      // Call the function initially to set the value
      resolveItemsToShow()

      return itemsToShow
    }
  }

// export default { LayoutHelpers }
