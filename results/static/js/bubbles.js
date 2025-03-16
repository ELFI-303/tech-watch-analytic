function bubbleStart(categoriesCount,start_date_query, end_date_query, start_date, end_date,input_search,AND,STRICT) {
    start_date_query = start_date_query.toISOString().split('T')[0];
    end_date_query = end_date_query.toISOString().split('T')[0];
    start_date = start_date.toISOString().split('T')[0];
    end_date = end_date.toISOString().split('T')[0];

    let clickCount = 0;
    const tripleClickDelay = 600;
    const counts = Object.values(categoriesCount);
    const maxCount = Math.max(...counts);
    const halfWindow = Math.min(window.innerHeight,window.innerWidth) / 2;
    Object.keys(categoriesCount).forEach(function(k){
        const diameter = (Math.sqrt(Math.sqrt(Math.sqrt(categoriesCount[k] / maxCount))) * halfWindow)/Math.sqrt(Math.sqrt(counts.length));
        const div = document.createElement('div');
        div.className = 'bubble';
        div.style.top = getRandomArbitrary(diameter*2,window.innerHeight-diameter*2)+'px';
        div.style.left = getRandomArbitrary(diameter*2,window.innerWidth-diameter*2)+'px';
        div.style.backgroundColor = getColor(k);
        div.style.color = 'white';
        div.style.width = diameter+'px';
        div.style.height = diameter+'px';
        div.innerHTML = '<div style="height:'+((parseFloat(div.style.width)/2)-parseFloat(div.style.width)/12)+'px;"></div><p style="font-weight:bold;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none; text-align: center;vertical-align: middle;font-size:'+parseFloat(div.style.width)/10+'px">'+k.toUpperCase()+'</p>';
        document.body.appendChild(div);
    });
    const bubbles = Array.from(document.querySelectorAll('.bubble'));
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;
    var gravityStrength = 0.3; // Constant gravity force
    const bounceFactor = 0.95; // Elasticity of the collisions

    const velocities = Array.from(bubbles).map(() => ({
        vx: 0, // Random initial velocity
        vy: 0
    }));
    document.addEventListener('keypress',(e) => {
        if (e.key === ' ') {
            const colors = [];
            const selectedBubbles = bubbles.filter(bubble => bubble.classList.contains('selected'));
            bubbles.forEach((bubble, index) => {
                if (bubble.classList.contains('selected')) {
                    bubbles.splice(index, 1);
                }
            });
            selectedBubbles.sort((a, b) => {
                const widthA = a.getBoundingClientRect().width;
                const widthB = b.getBoundingClientRect().width;
                return widthB - widthA;
            });
            selectedBubbles.forEach((bubble) => {
                const style = window.getComputedStyle(bubble);
                const color = style.backgroundColor;
                const opacity = 255 / selectedBubbles.length;
                const rgb = color.match(/\d+/g).map(Number);
                const r = rgb[0], g = rgb[1], b = rgb[2], a = opacity / 255;
                colors.push({ r, g, b, a });
            });
            processBubbles(selectedBubbles).then((categories) => {
                const minSize = selectedBubbles[selectedBubbles.length-1].getBoundingClientRect().width;
                blendedColor = blendColors(colors);
                const backgroundDiv = document.createElement('div');
                backgroundDiv.style.zIndex = 22+selectedBubbles.length;
                backgroundDiv.style.position = 'absolute';
                backgroundDiv.style.borderRadius = '50%';
                document.location.href.split('/')[3].split("?")[0] != "" ? backgroundDiv.style.backgroundColor = 'white' : backgroundDiv.style.backgroundColor = blendedColor;
                backgroundDiv.style.opacity = 1;
                backgroundDiv.style.width = `${minSize}px`;
                backgroundDiv.style.height = `${minSize}px`;
                backgroundDiv.style.left = `${(window.innerWidth / 2) - (minSize / 2)}px`;
                backgroundDiv.style.top = `${(window.innerHeight / 2) - (minSize / 2)}px`;
                document.body.appendChild(backgroundDiv);
                selectedBubbles.push(backgroundDiv);
                expandBubblesAndAct(selectedBubbles).then(() => {
                    // Use 'catFromExpand' instead of 'cat' to avoid shadowing the 'cat' from the outer scope
                    const baseUrl = categories.toString().replace(new RegExp(' ', 'g'), '_').replace(new RegExp('&', 'g'), '-');
                    const queryParams = `?start_date_query=${start_date_query}&end_date_query=${end_date_query}&start_date=${start_date}&end_date=${end_date}&and=${AND}&strict=${STRICT}`;
                    if (input_search == null || input_search == "" || input_search == "null" || input_search == " "  ){
                        const finalUrl = baseUrl + queryParams;
                        document.location.href.split('/')[3].split("?")[0] != "" ? location.href = "topics/"+finalUrl : location.href = finalUrl;
                    } else {
                        const finalUrl = baseUrl + queryParams + `&input_search=${input_search}`;
                        document.location.href.split('/')[3].split("?")[0] != "" ? location.href = "topics/"+finalUrl : location.href = finalUrl;
                    }
                });
            });
        }
    });
    bubbles.forEach((bubble) => {
        let isDragging = false;
        let shiftX, shiftY;

        // Get the index of the bubble for velocity access
        const index = Array.from(bubbles).indexOf(bubble);

        bubble.addEventListener("click", () => {
            clickCount++;

            setTimeout(() => {
                if (clickCount === 2) {
                    if (bubble.classList.contains('selected')){
                        bubble.classList.remove('selected');
                        bubble.style.outline = '';
                        bubble.style.textDecorationLine = '';
                        bubble.style.zIndex = 10;
                    } else {
                        bubble.classList.add('selected');
                        bubble.style.outline = '10px solid rgba(0, 0, 0, 0.51)';
                        bubble.style.textDecorationLine = 'underline';
                        bubble.style.zIndex = 20;
                    }
                } else if (clickCount === 3) {
                    bubble.style.zIndex = 70;
                    const category = bubble.textContent;
                    bubble.innerHTML = '';
                    const inter = setInterval(() => {
                        bubble.classList.add('expand');
                        const currentSize = parseFloat(bubble.style.width); 
                        const X = parseFloat(bubble.style.left); 
                        const Y = parseFloat(bubble.style.top); 
                        const newSize = currentSize * 1.04;
                        if (newSize >= 2*window.innerWidth){
                            clearInterval(inter);
                            document.location.href.split('/')[3].split("?")[0] != "" ? location.href = "topics/"+category.replace(new RegExp(' ', 'g'),'_').replace(new RegExp('&', 'g'),'-')+"?start_date_query="+start_date_query+"&end_date_query="+end_date_query+"&start_date="+start_date+"&end_date="+end_date+"&input_search="+input_search+"&and="+AND+"&strict="+STRICT : location.href = category.replace(new RegExp(' ', 'g'),'_').replace(new RegExp('&', 'g'),'-')+"?start_date_query="+start_date_query+"&end_date_query="+end_date_query+"&start_date="+start_date+"&end_date="+end_date+"&input_search="+input_search+"&and="+AND+"&strict="+STRICT;
                        }
                        bubble.style.left = `${X + (currentSize-newSize)/2}px`;
                        bubble.style.top = `${Y + (currentSize-newSize)/2}px`;
                        bubble.style.width = `${newSize}px`;
                        bubble.style.height = `${newSize}px`;
                    }, 8);
                }
                clickCount = 0;
            }, tripleClickDelay);
        });
        bubble.addEventListener('mousedown', function (e) {
            isDragging = true;

            shiftX = e.clientX - bubble.getBoundingClientRect().left;
            shiftY = e.clientY - bubble.getBoundingClientRect().top;

            bubble.classList.add('moving');

            // Disable gravity and velocity updates while dragging
            velocities[index].vx = 0;
            velocities[index].vy = 0;

            function moveAt(pageX, pageY) {
                bubble.style.left = pageX - shiftX + 'px';
                bubble.style.top = pageY - shiftY + 'px';
            }

            moveAt(e.pageX, e.pageY);

            function onMouseMove(event) {
                if (isDragging) {
                    moveAt(event.pageX, event.pageY);
                }
            }

            document.addEventListener('mousemove', onMouseMove);

            // Handle mouse up event to stop dragging
            document.addEventListener('mouseup',function () {
                    isDragging = false;
                    bubble.classList.remove('moving');
                    document.removeEventListener('mousemove', onMouseMove);

                    // Reinitialize velocity when dragging stops
                    const rect = bubble.getBoundingClientRect();
                    const bubbleCenterX = rect.left + rect.width / 2;
                    const bubbleCenterY = rect.top + rect.height / 2;

                    const dx = centerX - bubbleCenterX;
                    const dy = centerY - bubbleCenterY;

                    const angle = Math.atan2(dy, dx);

                    // Apply an initial velocity in the direction of gravity
                    velocities[index].vx = 0;
                    velocities[index].vy = 0;
                },
                { once: true }
            );
        });
        bubble.ondragstart = function () {
            return false; // Prevent default drag behavior
        };
    });

    // Update bubble positions
    function updateBubblePositions() {
        bubbles.forEach((bubble, index) => {
            if (bubble.classList.contains('moving')) return; // Skip moving bubbles

            const rect = bubble.getBoundingClientRect();
            const bubbleDiameter = rect.width;

            const maxLeft = window.innerWidth - bubbleDiameter;
            const maxTop = window.innerHeight - bubbleDiameter;

            var newLeft = rect.left + velocities[index].vx;
            var newTop = rect.top + velocities[index].vy;
            
            if ( newLeft > maxLeft || newLeft < 0) {
                velocities[index].vx = -velocities[index].vx;
                newLeft = rect.left + velocities[index].vx;
            }
            if ( newTop > maxTop || newTop < 0) {
                velocities[index].vy = -velocities[index].vy;
                newTop = rect.top + velocities[index].vy;
            }

            bubble.style.left = `${newLeft}px`;
            bubble.style.top = `${newTop}px`;
        });
    }

    // Check and handle collisions
    function handleCollisions() {
        for (let i = 0; i < bubbles.length; i++) {
            for (let j = i + 1; j < bubbles.length; j++) {
                if (bubbles[i].classList.value.includes('expand') || bubbles[j].classList.value.includes('expand')) {
                    break
                }
                const rectA = bubbles[i].getBoundingClientRect();
                const rectB = bubbles[j].getBoundingClientRect();
                const bubbleRadiusA = rectA.width / 2;
                const bubbleRadiusB = rectB.width / 2;

                const dx = (rectA.left + bubbleRadiusA) - (rectB.left + bubbleRadiusB);
                const dy = (rectA.top + bubbleRadiusA) - (rectB.top + bubbleRadiusB);
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < bubbleRadiusA + bubbleRadiusB) { // Collision detected
                    // Calculate the collision angle
                    const angle = Math.atan2(dy, dx);

                    // Minimum distance needed to prevent overlap
                    const minDistance = bubbleRadiusA + bubbleRadiusB;

                    // Calculate the separation needed
                    const overlap = minDistance - distance;

                    // Push bubbles apart to prevent continuous overlap
                    const separationX = (overlap / 2) * Math.cos(angle);
                    const separationY = (overlap / 2) * Math.sin(angle);

                    // Adjust positions to separate bubbles
                    newLeftA = parseFloat(bubbles[i].style.left || rectA.left) + separationX
                    newTopA = parseFloat(bubbles[i].style.top || rectA.top) + separationY
                    newLeftB = parseFloat(bubbles[j].style.left || rectB.left) - separationX
                    newTopB = parseFloat(bubbles[j].style.top || rectB.top) - separationY

                    bubbles[i].style.left = `${newLeftA}px`;
                    bubbles[i].style.top = `${newTopA}px`;
                    bubbles[j].style.left = `${newLeftB}px`;
                    bubbles[j].style.top = `${newTopB}px`;

                    // Exchange velocities (simple elastic collision)
                    const v1 = velocities[i];
                    const v2 = velocities[j];

                    // Project velocities onto collision axis
                    const collisionVector = { x: dx / distance, y: dy / distance };
                    const relativeVelocity = {
                        x: v1.vx - v2.vx,
                        y: v1.vy - v2.vy
                    };
                    const speed = relativeVelocity.x * collisionVector.x + relativeVelocity.y * collisionVector.y;

                    if (speed > 0) continue; // Skip if they are moving apart

                    // Apply bounce factor and adjust velocities
                    const impulse = (2 * speed) / (bubbleRadiusA + bubbleRadiusB);

                    // Get the diameters
                    const bubbleDiameterA = rectA.width;
                    const bubbleDiameterB = rectB.width;

                    // Get maximum parcours X and Y
                    const maxLeftA = window.innerWidth - bubbleDiameterA;
                    const maxTopA = window.innerHeight - bubbleDiameterA;
                    const maxLeftB = window.innerWidth - bubbleDiameterB;
                    const maxTopB = window.innerHeight - bubbleDiameterB;

                    if ( newLeftA > maxLeftA || newLeftA < 0) {
                        v1.vx += impulse * bubbleRadiusB * collisionVector.x * bounceFactor;
                    } else {
                        v1.vx -= impulse * bubbleRadiusB * collisionVector.x * bounceFactor;
                    }
                    if ( newTopA > maxTopA || newTopA < 0) {
                        v1.vy += impulse * bubbleRadiusB * collisionVector.y * bounceFactor;
                    } else {
                        v1.vy -= impulse * bubbleRadiusB * collisionVector.y * bounceFactor;
                    }
                    if ( newLeftB > maxLeftB || newLeftB < 0) {
                        v2.vx -= impulse * bubbleRadiusA * collisionVector.x * bounceFactor;
                    } else {
                        v2.vx += impulse * bubbleRadiusA * collisionVector.x * bounceFactor;
                    }
                    if ( newTopB > maxTopB || newTopB < 0) {
                        v2.vy -= impulse * bubbleRadiusA * collisionVector.y * bounceFactor;
                    } else {
                        v2.vy += impulse * bubbleRadiusA * collisionVector.y * bounceFactor;
                    }
                }
            }
        }
    }

    function applyTemporaryGravity() {
        const interval = setInterval(() => {
            gravityStrength -= 0.005
            bubbles.forEach((bubble, index) => {
                    if (gravityStrength <= 0) {
                        clearInterval(interval);
                        velocities[index].vx = velocities[index].vx/10;
                        velocities[index].vy = velocities[index].vx/10;
                    }
                    const rect = bubble.getBoundingClientRect();
                    const bubbleCenterX = rect.left + rect.width / 2;
                    const bubbleCenterY = rect.top + rect.height / 2;


                    const dx = centerX > bubbleCenterX ? centerX + window.innerWidth/2 - bubbleCenterX : centerX - window.innerWidth/2 - bubbleCenterX;
                    const dy = centerY > bubbleCenterY ? centerY + window.innerHeight - bubbleCenterY : centerY - window.innerHeight - bubbleCenterY;

                    const angle = Math.atan2(dy, dx);

                    // Apply gravity to velocity
                    velocities[index].vx += Math.cos(angle) * gravityStrength;
                    velocities[index].vy += Math.sin(angle) * gravityStrength;
            });
        }, 10);
    }

    applyTemporaryGravity();
    // Main update loop
    setInterval(() => {
        updateBubblePositions();
        handleCollisions();
    }, 8); // Roughly 60 FPS
};
