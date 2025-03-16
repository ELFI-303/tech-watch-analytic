
async function fetchCSV(url) {
    const response = await fetch("http://127.0.0.1:5000/"+url);
    return await response.json();
}
async function getCategories(start_date,end_date,input_search,and,strict) {
    if (input_search != null && input_search != "" && input_search != "null"  && input_search != " "){
        var data = await fetchCSV("search?start_date="+start_date+"&end_date="+end_date+"&input_search="+input_search+"&and="+and+"&strict="+strict);
    } else {
        var data = await fetchCSV("all?start_date="+start_date+"&end_date="+end_date);
    }
    const articles = JSON.parse(data);
    
    const categoriesCount = {};
    var dates = [];
    articles.forEach((article) => {
        const cats = JSON.parse(article.category.replace(/'/g, '"'));
        max = 0;
        cats.forEach((category) => {
            if (!categoriesCount[category]) {
                categoriesCount[category] = 0;
            }
            categoriesCount[category]++;
        });
        dates.push(article.date);
    });
    return new Promise((resolve) => {
        resolve([categoriesCount,dates]);
    });
}
async function getTopics(category,start_date,end_date,input_search,and,strict) {
    if (input_search != null && input_search != "" && input_search != "null" && input_search != " "){
        var data = await fetchCSV("search/"+category+"?start_date="+start_date+"&end_date="+end_date+"&input_search="+input_search+"&and="+and+"&strict="+strict);
    } else {
        var data = await fetchCSV("all/"+category+"?start_date="+start_date+"&end_date="+end_date);
    }
    const articles = JSON.parse(data);
    const topicsCount = {};
    var dates = [];
    articles.forEach((article) => {
        const topic = article.topic;
        if (!topicsCount[topic]) {
            topicsCount[topic] = 0;
        }
        topicsCount[topic]++;
        dates.push(article.date);
    });
    return new Promise((resolve) => {
        resolve([topicsCount,dates]);
    });
}
async function getArticles(topics,start_date,end_date,input_search,and,strict){
    if (input_search != null && input_search != "" && input_search != "null" && input_search != " "){
        var data = await fetchCSV("topics/search/"+topics+"?start_date="+start_date+"&end_date="+end_date+"&input_search="+input_search+"&and="+and+"&strict="+strict);
    } else {
        var data = await fetchCSV("topics/all/"+topics+"?start_date="+start_date+"&end_date="+end_date);
    }
    const articles = JSON.parse(data);
    return new Promise((resolve) => {
        resolve(articles);
    });
}
async function getStatisticNumber(articles){
    const request = new Request("http://127.0.0.1:5000/statistic/number", {
        method: "POST",
        body: JSON.stringify({ 
            articles: articles
        }),
    });
    const response = await fetch(request);
    const json_articles = response.json();
    return await json_articles;
}