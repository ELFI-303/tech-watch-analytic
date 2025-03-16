
function getColor(category) {
    switch (category.toUpperCase()){
        case 'ECOSYSTEM':
            return 'rgb(136, 176, 75)';
        case 'DEVOPS':
            return 'rgb(225, 93, 68)';
        case 'MIGRATION':
            return 'rgb(127, 205, 205)';
        case 'INFRASTRUCTURE':
            return 'rgb(102, 103, 171)';
        case 'SECURITY':
            return 'rgb(15, 76, 129)';
        case 'DB & BIG DATA':
            return 'rgb(146, 106, 166)';
        case 'ANALYTICS':
            return 'rgb(146, 106, 166)';
        case 'STORAGE':
            return 'rgb(240, 208, 0)';
        case 'APPLICATION':
            return 'rgb(210, 56, 108)';
        case 'AI & ML':
            return 'rgb(138, 43, 226)';
        case 'BUSINESS':
            return 'rgb(155, 35, 53)';
        case 'OTHER':
            return 'rgb(211, 211, 211)';
        default:
            const g = getRandomArbitrary(100,155);
            return 'rgb('+g+','+g+','+g+')';

        
    }
}
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}
function clearGraduation(){
    const graduation = document.querySelector(".graduation");
    while (graduation.firstChild) {
        graduation.removeChild(graduation.lastChild);
    }
}
function getGraduation(date,minTimeStamp,maxTimeStamp,format) {
    const graduation = document.querySelector(".graduation");

    const ratioDate = (date.getTime() - minTimeStamp) / (maxTimeStamp - minTimeStamp);
    const leftOffset = parseFloat(ratioDate) * parseFloat(graduation.getBoundingClientRect().width);

    const span = document.createElement('span');
    span.style.display = 'flex';
    span.style.justifyContent = 'center';
    span.style.height = '10px';
    span.style.borderRadius = '50%';
    span.style.background = 'rgb(29, 29, 29)';
    span.style.color = 'rgb(29, 29, 29)';
    span.style.fontSize = '10px';
    span.style.fontFamily = 'system-ui';
    span.style.position = 'absolute';
    span.style.left = leftOffset+'px';
    span.style.lineHeight = '40px';
    
    if ( format == 'year'){
        span.style.fontSize = '12px';
        span.style.lineHeight = '40px';
        span.style.height = '12px';
        span.style.width = '2px';
        span.innerText = date.toISOString().split('T')[0].split('-')[0];
    } else if ( format == 'month' ){
        span.style.width = '1px';
        span.innerText = date.toString().split(" ")[1];
    } else {
        const dateReturn = date.toISOString().split('T')[0].split('-');
        span.style.fontSize = '15px';
        span.style.lineHeight = '70px';
        span.style.height = '25px';
        span.style.width = '2px';
        span.className = format;
        span.innerText = dateReturn[2]+'/'+dateReturn[1]+'/'+dateReturn[0];
        if ( format == 'dateMin') {
            span.style.left = 0+'px';
        } else {
            span.style.left = parseFloat(graduation.getBoundingClientRect().width)+'px';
        }
    }
    graduation.appendChild(span);
}
function getDates(startDate, endDate) {
    var yearsArray = new Array();
    var monthsArray = new Array();
    var currentDate = endDate;
    while (currentDate <= startDate) {
        currentDate = new Date(currentDate);
        if (currentDate.toISOString().split("T")[0].split(new RegExp("-","g"))[2] == 1){
            dateParse = currentDate
            dateParse = new Date(dateParse);
            dateParse.setDate(dateParse.getDate())
            if (currentDate.getMonth() == 0){
                yearsArray.push(dateParse);
            } else {
                monthsArray.push(dateParse);
            }
        }
        currentDate.setDate(currentDate.getDate() + 1);
    }
    return [yearsArray,monthsArray];
}


function callMaj(start_date,end_date,category,input_search=null,and=null,strict=null) {
    if (start_date != undefined){
        start_date = start_date.toISOString().split('T')[0];
    }
    if (end_date != undefined){
        end_date = end_date.toISOString().split('T')[0];
    }

    if (document.location.href.split('/')[3].split("?")[0] != "") {
        return new Promise((resolve, reject) => {
            getTopics(category,start_date,end_date,input_search,and,strict).then((categories) => {
                const [categoriesCount,dates] = categories;
                resolve([categoriesCount,dates]);
            }).catch((error) => {
                reject(error);
            });
        });
    } else {
        return new Promise((resolve, reject) => {
            getCategories(start_date,end_date,input_search,and,strict).then((categories) => {
                const [categoriesCount,dates] = categories;
                resolve([categoriesCount,dates]);
            }).catch((error) => {
                reject(error);
            });
        });
    }
}
function blendColors(colorList) {
    // Start with a transparent black as the base
    let blended = { r: 0, g: 0, b: 0, a: 0 };

    colorList.forEach(({ r, g, b, a }) => {
        const alpha = a + blended.a * (1 - a);

        blended = {
            r: Math.round((r * a + blended.r * blended.a * (1 - a)) / alpha),
            g: Math.round((g * a + blended.g * blended.a * (1 - a)) / alpha),
            b: Math.round((b * a + blended.b * blended.a * (1 - a)) / alpha),
            a: alpha
        };
    });
    
    return `rgb(${blended.r}, ${blended.g}, ${blended.b}`;
}
function getSearch(){
    const inputSearch = document.querySelector('.input');
    const searchStyle = document.querySelector('.search-icon');
    const buttonAndOr = document.querySelector('.button-andor');
    const buttonStrCont = document.querySelector('.button-strcont');
    const dotAndOr = document.querySelector('.dot-andor');
    const dotStrCont = document.querySelector('.dot-strcont');
    var AND = true;
    var STRICT = true;
    inputSearch.addEventListener('focus',()=>{
        searchStyle.style.pointerEvents = 'all';
        searchStyle.style.cursor = 'pointer';
        searchStyle.style.transform = 'rotate(0deg)';
        buttonAndOr.style.width = '40px';
        buttonAndOr.style.opacity = 100;
        buttonStrCont.style.width = '40px';
        buttonStrCont.style.opacity = 100;
    })
    inputSearch.addEventListener('focusout',()=>{
        searchStyle.style.pointerEvents = 'none';
        searchStyle.style.cursor = 'default';
        searchStyle.style.transform = 'rotate(90deg)';
        buttonAndOr.style.width = '20px';
        buttonAndOr.style.opacity = 0;
        buttonStrCont.style.width = '20px';
        buttonStrCont.style.opacity = 0;
        
    })
    buttonAndOr.addEventListener('mousedown', (event) => {
        event.preventDefault();
        AND = !AND;
        if(AND){
            dotAndOr.style.backgroundColor = 'whitesmoke';
            buttonAndOr.style.backgroundColor = '#3f3f3f';
            dotAndOr.style.marginLeft = '5px';
            dotAndOr.innerHTML = 'AND';
        } else {
            dotAndOr.style.backgroundColor = '#3f3f3f';
            buttonAndOr.style.backgroundColor = 'whitesmoke';
            dotAndOr.style.marginLeft = buttonAndOr.getBoundingClientRect().width-dotAndOr.getBoundingClientRect().width-5+'px';
            dotAndOr.innerHTML = 'OR';
        }
    });
    buttonStrCont.addEventListener('mousedown', (event) => {
        event.preventDefault();
        STRICT = !STRICT;
        if(STRICT){
            dotStrCont.style.backgroundColor = 'whitesmoke';
            buttonStrCont.style.backgroundColor = '#3f3f3f';
            dotStrCont.style.marginLeft = '5px';
            dotStrCont.innerHTML = 'STRICT';
        }else{
            dotStrCont.style.backgroundColor = '#3f3f3f';
            buttonStrCont.style.backgroundColor = 'whitesmoke';
            dotStrCont.style.marginLeft = buttonStrCont.getBoundingClientRect().width-dotStrCont.getBoundingClientRect().width-5+'px';
            dotStrCont.innerHTML = 'CONTAIN';
        }
    })
}
function searchArticles(input_search,and,strict){
    const inputSearch = document.querySelector('.input');
    var AND_query,STRICT_query;
    var dotAndOr = document.querySelector('.dot-andor');
    var dotStrCont = document.querySelector('.dot-strcont');
    
    dotAndOr.innerHTML == 'AND' ? AND_query = true : AND_query = false;
    dotStrCont.innerHTML == 'STRICT' ? STRICT_query = true : STRICT_query = false;
    
    var new_articles = []
    return new Promise((resolve, reject) => {
        CallArticleList(start_date,end_date,topics,input_search,and,strict).then((articles)=>{
            articles.forEach((article)=>new_articles.push(article)); 
            if (inputSearch.value == null || inputSearch.value == "") {
                return new_articles;
            }
            const searchTerms = inputSearch.value.split(" ");
            data = [];
            new_articles.forEach((article) => {
                if (article.corp == null){
                    return;
                }
                const articleText = article.corp.toLowerCase()+article.title.toLowerCase();
                let matches = searchTerms.map(term => {
                    if (STRICT_query) {
                    // Strict match (whole word)
                    const regex = new RegExp(`\\b${term.toLowerCase()}\\b`);
                    return regex.test(articleText);
                    } else {
                    // Partial match
                    return articleText.includes(term.toLowerCase());
                    }
                });
            
                // Combine matches based on logic type
                const isMatch = AND_query === true ? matches.every(Boolean) : matches.some(Boolean);
                if (isMatch){
                    data.push(article);
                } else {
                    return;
                }
            });
            resolve(data);
        })
    });

}
function searchQuery(){
    const inputSearch = document.querySelector('.input');
    var AND,STRICT;
    var dotAndOr = document.querySelector('.dot-andor');
    var dotStrCont = document.querySelector('.dot-strcont');
    dotAndOr.innerHTML == 'AND' ? AND = true : AND = false;
    dotStrCont.innerHTML == 'STRICT' ? STRICT = true : STRICT = false;
    sliderStart(minTimeStamp,maxTimeStamp,start_date,end_date,category,inputSearch.value,AND,STRICT);
}
function expandBubblesAndAct(selectedBubbles) {
    // Wrap each iteration in a Promise
    const promises = selectedBubbles.map((bubble, index) => {
        return new Promise((resolve) => {

            // Delay each bubble's expansion by a time based on its index (staggered animation)
            setTimeout(() => {
                const inter = setInterval(() => {
                    bubble.classList.add('expand');
                    const currentSize = parseFloat(bubble.getBoundingClientRect().width);
                    const X = parseFloat(bubble.style.left);
                    const Y = parseFloat(bubble.style.top);
                    const newSize = currentSize * 1.04;

                    // Stop the animation when the bubble reaches twice the width of the screen
                    if (newSize >= 2 * window.innerWidth) {
                        clearInterval(inter);
                        resolve(); // Resolve this bubble's Promise when the animation stops
                    }

                    // Adjust bubble position to keep it centered
                    bubble.style.left = `${X + (currentSize - newSize) / 2}px`;
                    bubble.style.top = `${Y + (currentSize - newSize) / 2}px`;
                    bubble.style.width = `${newSize}px`;
                    bubble.style.height = `${newSize}px`;
                }, 8);
            }, index * 1000 / selectedBubbles.length);
        });
    });
    // Wait for all bubbles to finish expanding
    return Promise.all(promises);
}
function goBackEvent(){
    const goBack = document.querySelector('.left-arrow-div');
    goBack.addEventListener('mouseover', () => {
        if (!mooving){
            mooving = true;
            const positions = [];
            for (let j = 20; j >= 1; j--) {
                positions.push(j);
            }
            for (let i = 0; i <= 19; i++) {
                positions.push(i);
            }

            let index = 0;
            const interval = setInterval(() => {
                goBack.addEventListener('mouseleave', () => {
                    clearInterval(interval);
                    arrow.style.opacity = 0;
                    mooving = false;
                });
                if (index >= positions.length) {
                    index = 0;
                }
                arrow.style.opacity = Math.abs(positions[index]*5-100)/100;
                arrow.style.marginLeft = positions[index] + 'px';
                index++;
            }, 60);

        }

    });
    goBack.addEventListener('click', () => location.href = "/");
}

function animateToCenter(bubble,opacity) {
    return new Promise((resolve) => {
        const rect = bubble.getBoundingClientRect();
        const startX = rect.left;
        const startY = rect.top;
        const targetX = (window.innerWidth / 2) - (rect.width / 2);
        const targetY = (window.innerHeight / 2) - (rect.height / 2);
        const duration = 500; // Animation duration in milliseconds
        const startTime = Date.now(); // Capture the start time

        const interval = 16; // Update every 16ms for ~60 FPS
        const timer = setInterval(() => {
            bubble.classList.add('expand');
            const elapsed = Date.now() - startTime; // Get elapsed time
            const progress = Math.min(elapsed / duration, 1); // Normalize progress to [0, 1]
            // Interpolate position
            const currentX = startX + (targetX - startX) * progress;
            const currentY = startY + (targetY - startY) * progress;

            bubble.style.opacity = 1-(1-opacity)*progress;
            bubble.style.left = `${currentX}px`;
            bubble.style.top = `${currentY}px`;

            if (progress >= 1) {
                clearInterval(timer); // Stop the animation when it's done
                resolve(); // Resolve the promise when the animation is complete
            }
        }, interval); // Run the animation at intervals of `interval` milliseconds
    });
}

function processBubbles(selectedBubbles) {
    const colors = [];
    let zIndex = 21; // Adjust z-index starting point
    let minSize = Number.MAX_VALUE; // For tracking the minimum bubble size

    const categories = [];
    const bubblePromises = selectedBubbles.map((bubble) => {
        categories.push(bubble.textContent);
        const style = window.getComputedStyle(bubble);
        const color = style.backgroundColor;
        const opacity = 255 / selectedBubbles.length;
        const rgb = color.match(/\d+/g).map(Number);
        const r = rgb[0], g = rgb[1], b = rgb[2], a = opacity / 255;
        colors.push({ r, g, b, a });

        const rect = bubble.getBoundingClientRect();
        minSize = Math.min(minSize, rect.width);

        //bubble.classList.add(bubble.textContent.replace(new RegExp(' ','g'),'_'));
        bubble.innerHTML = '';
        bubble.style.outline = '';
        bubble.style.boxShadow = '';
        bubble.style.zIndex = zIndex;
        zIndex++;

        // Animate each bubble and return the promise
        return animateToCenter(bubble,1 / selectedBubbles.length);
    });
    return Promise.all(bubblePromises).then(() => categories);
}
function CallArticleList(start_date,end_date,topics,input_search=null,and=null,strict=null) {
    if (start_date != undefined){
        start_date = start_date.toISOString().split('T')[0];
    }
    if (end_date != undefined){
        end_date = end_date.toISOString().split('T')[0];
    }
    return new Promise((resolve, reject) => {
        getArticles(topics,start_date,end_date,input_search,and,strict).then((articles) => {
            resolve(articles);
        }).catch((error) => {
            reject(error);
        });
    });
}