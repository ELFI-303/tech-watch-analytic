function checkRes(article,res){
    i = new Date(article.date);
    var year = i.getFullYear();
    var firstDayOfTheYear = new Date(year, 0, 1);
    var days = Math.floor((i - firstDayOfTheYear) / (24 * 60 * 60 * 1000));
    var week = Math.ceil((i.getDay() + 1 + days) / 7);
    var weekYear = week + '/' + year;
    if (weekYear == res){
        return true;
    } else {
        return false;
    }
}
function getMonday(d) {
    d = new Date(d);
    var day = d.getDay(),
      diff = d.getDate() - day + (day == 0 ? -6 : 1); // adjust when day is sunday
    return new Date(d.setDate(diff));
}
function getDaysWeek(firstDayWeek,lastDayWeek) {
    let dates_list = [];
    while(firstDayWeek <= lastDayWeek){
        const dateToPush = new Date(firstDayWeek).toISOString().split('T')[0].split('-');
        dates_list.push(dateToPush[2]+"/"+dateToPush[1]);
        firstDayWeek.setDate(firstDayWeek.getDate()+1);
    }
    return dates_list;
}
function getDatesNumberArticles(data){
    return new Promise((resolve, reject) => {
        getStatisticNumber(data).then((categories) => {
            const articles_list = categories;
            var articles = [];
            var dates = [];
            var topicsCount = {};
            var categoriesCount = {};
            for (const [weekYear, article] of Object.entries(articles_list)) {
                dates.push(weekYear);
                articles.push(article.length);
                article.forEach((arti)=> {
                    const topic = arti.topic;
                    const cats = JSON.parse(arti.category.replace(/'/g, '"'));
                    if (!topicsCount[topic]) {
                        topicsCount[topic] = 0;
                    }
                    cats.forEach((category) => {
                        if (!categoriesCount[category]) {
                            categoriesCount[category] = 0;
                        }
                        categoriesCount[category]++;
                    });
                    topicsCount[topic]++;
                })
            }
            const lastWeek = Object.values(articles_list)[Object.values(articles_list).length-1];
            const firstDayWeek = getMonday(lastWeek[0].date);
            const lastDayWeek = new Date(firstDayWeek);
            lastDayWeek.setDate(firstDayWeek.getDate()+6);
            var lastWeekDates = getDaysWeek(firstDayWeek,lastDayWeek);
            var lastWeekArticles = [];
            lastWeekDates.forEach((date)=>{
                let total = 0;
                lastWeek.forEach((article)=>{
                    const articleDate = new Date(article.date).toISOString().split('T')[0].split('-');
                    if (articleDate[2]+"/"+articleDate[1] === date){
                        total++;
                    }
                });
                lastWeekArticles.push(total);
            });
            topicsCount = Object.fromEntries(Object.entries(topicsCount).sort((a, b) => b[1] - a[1]));
            categoriesCount = Object.fromEntries(Object.entries(categoriesCount).sort((a, b) => b[1] - a[1]));
            resolve([articles,dates,topicsCount,categoriesCount,lastWeekDates,lastWeekArticles])
        }).catch((error) => {
            reject(error);
        });
    });
}

function resizeCanvas(canvas,width,height) {
    // Set canvas width and height to match the parent div
    canvas.width = width;
    canvas.height = height;
}
function calculateMovingAverage(data, windowSize) {
    const smoothed = [];
    for (let i = 0; i < data.length; i++) {
        const start = Math.max(0, i - windowSize + 1);
        const window = data.slice(start, i + 1);
        const average = window.reduce((sum, val) => sum + val, 0) / window.length;
        smoothed.push(average);
    }
    return smoothed;
}
/*
const dota = {
    labels: dates,
    datasets: [{
        label: 'Number of articles',
        data: articles,
        backgroundColor: 'rgba(75, 192, 192, 0.2)', // Optional for a line chart
        borderColor: 'rgba(75, 192, 192, 1)', // Color for the line
        borderWidth: 2, // Thickness of the line
        fill: false
    }]
};

instance = new Chart(ctx, {
    type: 'line', // Change from 'bar' to 'line'
    data: dota,
    options: {
        responsive: false
    }
});
const [articles,dates] = result;
const canvas = document.getElementById('myChart');
const ctx = canvas.getContext('2d');
*/
function setCanva(data,instances){
    return new Promise((resolve,reject) => {
        instances.forEach((instance)=>{
            if (instance instanceof Chart) {
                instance.destroy(); // Destroy the existing chart instance
            }
        })
        getDatesNumberArticles(data).then((result) => {
            const [articles,dates,topicsCount,categoriesCount,lastWeekDates,lastWeekArticles] = result;

            instances = [
                numberArticlesChart(dates,articles),
                categoriesCountChart(categoriesCount),
                topicsCountChart(topicsCount),
                lastWeekChart(lastWeekDates,lastWeekArticles)
            ];

            resolve(instances);
        }).catch((error) => {
            reject(error); // Catch any errors during the data fetch or chart creation
        });
    });
}
function numberArticlesChart(dates,articles){
    const canvas = document.getElementById('number-article-chart');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dota = {
        labels: dates,
        datasets: [{
            label: 'Number of articles',
            data: articles,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };
    return new Chart(ctx, {
        type: 'bar',
        data: dota,
        options: {
            responsive: false
        }
    });
}
function categoriesCountChart(categoriesCount){
    const canvas = document.getElementById('categories-count-chart');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dota = {
        labels: Object.keys(categoriesCount),
        datasets: [{
            label: 'Categories count',
            data: Object.values(categoriesCount),
            backgroundColor: 'rgba(75, 192, 114, 0.2)',
            borderColor: 'rgb(75, 192, 114)',
            borderWidth: 1
        }]
    };
    return new Chart(ctx, {
        type: 'bar',
        data: dota,
        options: {
            responsive: false
        }
    });
}
function topicsCountChart(topicsCount){
    const canvas = document.getElementById('topics-count-chart');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dota = {
        labels: Object.keys(topicsCount).map(date => date.length > 10 ? date.substring(0, 10) + '...' : date),
        datasets: [{
            label: 'Topics count',
            data: Object.values(topicsCount),
            backgroundColor: 'rgba(157, 192, 75, 0.2)',
            borderColor: 'rgb(157, 192, 75)',
            borderWidth: 1
        }]
    };
    return new Chart(ctx, {
        type: 'bar',
        data: dota,
        options: {
            responsive: false
        }
    });
}

function lastWeekChart(lastWeekDates,lastWeekArticles){
    const canvas = document.getElementById('last-week-chart');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dota = {
        labels: lastWeekDates,
        datasets: [{
            label: 'Latest week articles',
            data: lastWeekArticles,
            backgroundColor: 'rgba(192, 155, 75, 0.2)',
            borderColor: 'rgb(192, 155, 75)',
            borderWidth: 1
        }]
    };
    return new Chart(ctx, {
        type: 'bar',
        data: dota,
        options: {
            responsive: false
        }
    });
}