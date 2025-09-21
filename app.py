from flask import Flask, render_template, redirect, url_for
from data import photos


app = Flask(__name__)

# მთავარი გვერდი
@app.route("/")
def home():
    return render_template("index.html")

# მეორე გვერდი (მაგ: About)
@app.route("/about")
def about():
    return render_template("about.html")

# მეორე გვერდი (მაგ: About)
@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/photo/<int:photo_id>")
def photo_details(photo_id):
    photo = next((p for p in photos if p["id"] == photo_id), None)
    if not photo:
        return "Photo not found", 404
    return render_template("photo_details.html", photo=photo)

@app.route("/jets")
def jet_posters():
    # გაფილტრეთ `photos` სია, რათა მიიღოთ მხოლოდ `jet` კატეგორიის პოსტერები
    jet_photos = [p for p in photos if p["category"] == "jet"]

    # დააბრუნეთ ახალი HTML გვერდი და გადაეცით მას გაფილტრული სია
    return render_template("jet_posters.html", photos=jet_photos)

@app.route("/sport")
def sport_posters():
    # გაფილტრე პოსტერები კატეგორიის მიხედვით
    sport_photos = [p for p in photos if p.get("category") == "sport"]

    # დააბრუნე ახალი HTML გვერდი და გადაეცი მას გაფილტრული სია
    return render_template("sport_posters.html", photos=sport_photos)

@app.route("/retro")
def retro_posters():
    # გაფილტრე პოსტერები კატეგორიის მიხედვით
    retro_photos = [p for p in photos if p["category"] == "retro"]

    # დააბრუნე ახალი HTML გვერდი და გადაეცი მას გაფილტრული სია
    return render_template("retro_posters.html", photos=retro_photos)

@app.route("/cars")
def car_posters():
    # გაფილტრე პოსტერები კატეგორიის მიხედვით
    car_photos = [p for p in photos if p["category"] == "cars"]

    # დააბრუნე ახალი HTML გვერდი და გადაეცი მას გაფილტრული სია
    return render_template("cars_posters.html", photos=car_photos)

@app.route("/3d_models")
def three_d_models():
    # გაფილტრეთ `photos` სია, რათა მიიღოთ მხოლოდ `3d_model` კატეგორიის პოსტერები
    three_d_models_list = [p for p in photos if p["category"] == "3d_model"]

    # დააბრუნეთ ახალი HTML გვერდი და გადაეცით მას გაფილტრული სია
    return render_template("3d_models.html", photos=three_d_models_list)

@app.route("/my-website")
def my_website_posters():
    # გაფილტრე პოსტერები კატეგორიის მიხედვით
    my_website_photos = [p for p in photos if p["category"] == "my website"]

    # დააბრუნე ახალი HTML გვერდი და გადაეცი მას გაფილტრული სია
    return render_template("my_website_posters.html", photos=my_website_photos)

@app.route("/art")
def art_posters():
    # გაფილტრე პოსტერები კატეგორიის მიხედვით
    art_photos = [p for p in photos if p["category"] == "art"]

    # დააბრუნე ახალი HTML გვერდი და გადაეცი მას გაფილტრული სია
    return render_template("art_posters.html", photos=art_photos)

@app.route("/logo")
def logo_posters():
    # გაფილტრე პოსტერები კატეგორიის მიხედვით
    logo_photos = [p for p in photos if p["category"] == "logo"]

    # დააბრუნე ახალი HTML გვერდი და გადაეცი მას გაფილტრული სია
    return render_template("logo_posters.html", photos=logo_photos)

if __name__ == "__main__":
    app.run(debug=True)
