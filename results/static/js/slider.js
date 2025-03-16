function sliderStart(minTimeStamp,maxTimeStamp,start_date,end_date,category=null,input_search=null,and=null,strict=null) {
    const counterArticles = document.querySelector('.article-counter');

    function dateToReturn(date){
        const dateReturn = new Date(date).toISOString().split('T')[0].split('-');
        return dateReturn[2]+'/'+dateReturn[1]+'/'+dateReturn[0];
    }
    function controlFromSlider(fromSlider, toSlider) {
      const [from, to] = getParsed(fromSlider, toSlider);
      fillSlider(fromSlider, toSlider, '#C6C6C6', '#3f3f3f', toSlider);
      if (from > to) {
        fromSlider.value = to;
        dateMax.innerHTML = dateToReturn(to);
      } else {
        dateMin.innerHTML = dateToReturn(from);
      }
    }
    
    function controlToSlider(fromSlider, toSlider) {
      const [from, to] = getParsed(fromSlider, toSlider);
      fillSlider(fromSlider, toSlider, '#C6C6C6', '#3f3f3f', toSlider);
      setToggleAccessible(toSlider);
      if (from <= to) {
        toSlider.value = to;
        dateMax.innerHTML = dateToReturn(to);
      } else {
        dateMin.innerHTML = dateToReturn(from);
        toSlider.value = from;
      }
    }
    
    function getParsed(currentFrom, currentTo) {
      const from = parseInt(currentFrom.value, 10);
      const to = parseInt(currentTo.value, 10);
      return [from, to];
    }
    let debounceTimeout = null;

    function fillSlider(from, to, sliderColor, rangeColor, controlSlider) {
        const rangeDistance = to.max - to.min;
        const fromPosition = from.value - to.min;
        const toPosition = to.value - to.min;

        // Convert slider values to date objects for query
        let start_date_query = new Date(parseFloat(to.value));
        let end_date_query = new Date(parseFloat(from.value));

        if (start_date_query === start_date) {
            start_date_query = new Date(maxTimeStamp);
        }
        if (end_date_query === end_date) {
            end_date_query = new Date(minTimeStamp);
        }

        // Clear any existing debounce timeout
        clearTimeout(debounceTimeout);

        // Set a new debounce timeout
        debounceTimeout = setTimeout(() => {
            // Query backend after user stops moving the slider for 1 second
            callMaj(start_date_query, end_date_query, category, input_search, and, strict)
                .then((categories) => {
                    // Remove existing bubbles
                    const bubbles = document.querySelectorAll('.bubble');
                    bubbles.forEach((bubble) => bubble.remove());

                    // Process and display the data
                    const [categoriesCount, dates] = categories;
                    const minTimeStamp = Math.min(...dates);
                    const maxTimeStamp = Math.max(...dates);

                    let total = dates.length;

                    counterArticles.innerHTML = `Total: ${total} articles`;
                    bubbleStart(categoriesCount, start_date_query, end_date_query, start_date, end_date,input_search, and, strict);
                })
                .catch((error) => {
                    console.error("Error retrieving categories:", error);
                });
        }, 100); // Delay of 1 decisecond

        // Update the slider's visual background
        const fromPercent = (fromPosition / rangeDistance) * 100;
        const toPercent = (toPosition / rangeDistance) * 100;
        controlSlider.style.background = `linear-gradient(
            to right,
            ${sliderColor} 0%,
            ${sliderColor} ${fromPercent}%,
            ${rangeColor} ${fromPercent}%,
            ${rangeColor} ${toPercent}%, 
            ${sliderColor} ${toPercent}%, 
            ${sliderColor} 100%)`;
    }

    
    function setToggleAccessible(currentTarget) {
      const toSlider = document.querySelector('#toSlider');
      if (Number(currentTarget.value) <= 0 ) {
        toSlider.style.zIndex = 2;
      } else {
        toSlider.style.zIndex = 0;
      }
    }
    // Initialization
    const minDate = new Date(minTimeStamp);
    const maxDate = new Date(maxTimeStamp);

    clearGraduation();
    const graduation = document.querySelector(".graduation");
    const rangeBar = document.querySelector(".range");
    graduation.style.width = 1800;
    const offBy = (graduation.getBoundingClientRect().height)/4;
    graduation.style.left = offBy+'px';
    graduation.style.width = (rangeBar.getBoundingClientRect().width-offBy*2.75)+'px';
    getGraduation(minDate,end_date.getTime(),start_date.getTime(),'dateMin');
    getGraduation(maxDate,end_date.getTime(),start_date.getTime(),'dateMax');
    const dateMin = document.querySelector('.dateMin');
    const dateMax = document.querySelector('.dateMax');
    const [yearDates,monthDates] = getDates(start_date,end_date);
    yearDates.forEach((date) => {
        getGraduation(date,end_date.getTime(),start_date.getTime(),'year');
    })
    monthDates.forEach((date) => {
        getGraduation(date,end_date.getTime(),start_date.getTime(),'month');
    })

    const fromSlider = document.querySelector("#fromSlider");
    const toSlider = document.querySelector("#toSlider");

    fromSlider.min = end_date.getTime();
    toSlider.min = end_date.getTime();
    fromSlider.max = start_date.getTime();
    toSlider.max = start_date.getTime();
    fromSlider.value = minTimeStamp;
    toSlider.value = maxTimeStamp;

    // Regular behavior
    fillSlider(fromSlider, toSlider, '#C6C6C6', '#3f3f3f', toSlider);
    setToggleAccessible(toSlider);
    fromSlider.oninput = () => controlFromSlider(fromSlider, toSlider);
    toSlider.oninput = () => controlToSlider(fromSlider, toSlider);
}