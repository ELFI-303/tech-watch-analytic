from flask import Flask, request, jsonify, render_template
from datetime import datetime,timedelta
import pandas as pd
import json
from collections import OrderedDict

app = Flask(__name__)

# Sample data
data = pd.read_csv('data.csv',sep='§',engine='python',index_col=0)
data['date'] = pd.to_datetime(data['date'], dayfirst=True)
data_soft = data.drop(['corp','processed'],axis=1)
data = data.drop(['processed'],axis=1)

def parseDate() -> datetime:
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    return start_date,end_date

@app.route("/all/<category>", methods=["GET"])
def get_all_category(category):
    if len(category.split(",")) >= 1:
        category = category.split(",")
    else:
        category = list(category)
    start_date,end_date = parseDate()
    filtered_list = [item[1:-1] for item in data_soft['category'].tolist() if  any(cat.lower() in item.lower() for cat in category)]
    filtered_list = list(dict.fromkeys(filtered_list))
    filtered_data = data_soft[(data_soft['date'] >= end_date) & (data_soft['date'] <= start_date)]
    print('datasoft')
    print(data)
    for i in range(len(filtered_list)):
        filtered_list[i] = f"[{filtered_list[i]}]"
    print(filtered_list)
    filtered_data = filtered_data[filtered_data['category'].isin(filtered_list)]
    print(filtered_data)
    filtered_data.reset_index(inplace=True)
    return jsonify(filtered_data.to_json(orient='records'))

@app.route("/all", methods=["GET"])
def get_all():
    if request.args.get("start_date") != None and request.args.get("start_date") != "undefined":
        start_date,end_date = parseDate()
        filtered_data = data_soft[(data_soft['date'] >= end_date) & (data_soft['date'] <= start_date)]
        filtered_data.reset_index(inplace=True)
    else:
        filtered_data = data_soft
    print("all")
    print(filtered_data)
    return jsonify(filtered_data.to_json(orient='records'))

@app.route("/search/<category>", methods=["GET"])
def get_search_category(category):
    if len(category.split(",")) >= 1:
        category = category.split(",")
    else:
        category = list(category)

    start_date,end_date = parseDate()
    filtered_list = [item[1:-1] for item in data_soft['category'].tolist() if any(cat.lower() in item.lower() for cat in category)]
    filtered_list = list(dict.fromkeys(filtered_list))
    filtered_data = data[(data['date'] >= end_date) & (data['date'] <= start_date)]
    for i in range(len(filtered_list)):
        filtered_list[i] = f"[{filtered_list[i]}]"
    filtered_data = filtered_data[filtered_data['category'].isin(filtered_list)]
    inputs_search = request.args.get("input_search").split(" ")
    if request.args.get("strict") == 'true':
        if request.args.get("and") == 'true':
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: all(word.lower() in str(x).lower().split(" ") for word in inputs_search))]
        else:
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: any(word.lower() in str(x).lower().split(" ") for word in inputs_search))]
    else:
        if request.args.get("and") == 'true':
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: all(word.lower() in str(x).lower() for word in inputs_search))]
        else:
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: any(word.lower() in str(x).lower() for word in inputs_search))]
    filtered_data = filtered_data.drop(['corp'],axis=1)
    filtered_data.reset_index(inplace=True)
    return jsonify(filtered_data.to_json(orient='records'))

@app.route("/search", methods=["GET"])
def get_search():
    inputs_search = request.args.get("input_search").split(" ")
    if request.args.get("start_date") != None and request.args.get("start_date") != "undefined":
        start_date,end_date = parseDate()
        filtered_data = data[(data['date'] >= end_date) & (data['date'] <= start_date)]
        filtered_data.reset_index(inplace=True)
    else:
        filtered_data = data
    if request.args.get("strict") == 'true':
        if request.args.get("and") == 'true':
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: all(word.lower() in str(x).lower().split(" ") for word in inputs_search))]
        else:
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: any(word.lower() in str(x).lower().split(" ") for word in inputs_search))]
    else:
        if request.args.get("and") == 'true':
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: all(word.lower() in str(x).lower() for word in inputs_search))]
        else:
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: any(word.lower() in str(x).lower() for word in inputs_search))]
    filtered_data = filtered_data.drop(['corp'],axis=1)
    return jsonify(filtered_data.to_json(orient='records'))


@app.route("/", methods=["GET"])
def get_home():
    return render_template('test.html')

@app.route("/<categories>", methods=["GET"])
def get_category(categories: str):
    et = request.args.get("and")
    strict = request.args.get("strict")
    start_date,end_date = parseDate()
    inputs_search = request.args.get("input_search")
    if inputs_search == None:
        inputs_search = " "
    try:
        start_date_query = datetime.strptime(request.args.get("start_date_query"), "%Y-%m-%d")
        end_date_query = datetime.strptime(request.args.get("end_date_query"), "%Y-%m-%d")
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    return render_template('category.html', categories=categories,  start_date_query=start_date_query, end_date_query=end_date_query, start_date=start_date, end_date=end_date, inputs_search=inputs_search, et=et, strict=strict)
#MT,STORAGE,COREINFRASTRUCTUREANDSECURITYBLOG,THREAT-INTELLIGENCE,MICROSOFT-ENTRA-BLOG?start_date_query=2024-12-24&end_date_query=2022-01-03&start_date=2024-12-25&end_date=2022-01-02&input_search=

@app.route("/topics/<topics>", methods=["GET"])
def get_topics(topics: str):
    et = request.args.get("and")
    strict = request.args.get("strict")
    start_date,end_date = parseDate()
    inputs_search = request.args.get("input_search")
    if inputs_search == None:
        inputs_search = ""
    try:
        start_date_query = datetime.strptime(request.args.get("start_date_query"), "%Y-%m-%d")
        end_date_query = datetime.strptime(request.args.get("end_date_query"), "%Y-%m-%d")
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    return render_template('topics.html', topics=topics,  start_date_query=start_date_query, end_date_query=end_date_query, start_date=start_date, end_date=end_date, inputs_search=inputs_search, et=et, strict=strict)

@app.route("/topics/search/<topics>", methods=["GET"])
def get_search_topics(topics):
    if len(topics.split(",")) >= 1:
        topics = topics.split(",")
    else:
        topics = list(topics)
    start_date,end_date = parseDate()
    filtered_list = [item for item in data['topic'].tolist() if any(topic.lower() == item.lower() for topic in topics)]
    filtered_list = list(dict.fromkeys(filtered_list))
    filtered_data = data[(data['date'] >= end_date) & (data['date'] <= start_date)]
    filtered_data = filtered_data[filtered_data['topic'].isin(filtered_list)]
    inputs_search = request.args.get("input_search").split(" ")
    if request.args.get("strict") == 'true':
        if request.args.get("and") == 'true':
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: all(word.lower() in str(x).lower().split(" ") for word in inputs_search))]
        else:
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: any(word.lower() in str(x).lower().split(" ") for word in inputs_search))]
    else:
        if request.args.get("and") == 'true':
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: all(word.lower() in str(x).lower() for word in inputs_search))]
        else:
            filtered_data = filtered_data[filtered_data['corp'].apply(lambda x: any(word.lower() in str(x).lower() for word in inputs_search))]
    filtered_data.reset_index(inplace=True)
    return jsonify(filtered_data.to_json(orient='records'))

@app.route("/topics/all/<topics>", methods=["GET"])
def get_all_topics(topics):
    if len(topics.split(",")) >= 1:
        topics = topics.split(",")
    else:
        topics = list(topics)
    start_date,end_date = parseDate()
    filtered_list = [item for item in data['topic'].tolist() if  any(topic.lower() == item.lower() for topic in topics)]
    filtered_list = list(dict.fromkeys(filtered_list))
    filtered_data = data[(data['date'] >= end_date) & (data['date'] <= start_date)]
    filtered_data = filtered_data[filtered_data['topic'].isin(filtered_list)]
    filtered_data.reset_index(inplace=True)
    return jsonify(filtered_data.to_json(orient='records'))

@app.route("/statistic/number", methods=["POST"])
def get_statistic_number():
    articles = request.get_json(force=True)
    filtered_data = pd.DataFrame.from_dict(articles['articles'], orient='columns').reset_index(drop=True)
    filtered_data['date'] = pd.to_datetime(filtered_data['date'], unit='ms')
    grouped_articles = {}
    for index,article in filtered_data.iterrows():
        iso_year, iso_week, _ = article['date'].isocalendar()
        week_year = f"{iso_week}/{iso_year}"
        
        if week_year not in grouped_articles:
            grouped_articles[week_year] = []
        
        grouped_articles[week_year].append(article.to_dict())
    sorted_grouped_articles = OrderedDict(
        sorted(grouped_articles.items(), key=lambda x: (int(x[0].split('/')[1]), int(x[0].split('/')[0])))
    )
    return json.dumps(sorted_grouped_articles, indent=4, default=str)

if __name__ == "__main__":
    app.run(debug=True)