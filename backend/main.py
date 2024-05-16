from flask import Flask,request


#define a flask application 
app=Flask(__name__)

#hellow world 
@app.route("/hello")
def hello_fun():
    return ("Hellow ani \n")


#creating a global variable to store recipe this is our data store 
recipes = []

#API to fetch recipie 
@app.route("/fetch_recipes")
def recipies_fetch():
    #fetch out recipie form the data store 
    #return the the fetched recipie to the clinte 
    return recipes


#API to uplode recipie

@app.route("/uplode_recipes", methods=["POST"])
def recipie_upload_fn():
    #recive the dict sent by client 
    data=request.get_json()
    #add it to recipe list
    recipes.append(data)

    return "recipe uploded succesfully !"

    








if __name__ == "__main__" :
    app.run(debug=True)


