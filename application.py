from flask import Flask, request, render_template, redirect
from instamojo_wrapper import Instamojo
API_KEY = "test_e7d10a1857a494fd016051d8fcd"
AUTH_TOKEN = "test_d5264a300fc5205c2de74859588"

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,
                endpoint="https://test.instamojo.com/api/1.1/")
application = Flask(__name__)


@application.route("/")
@application.route("/index")
def index():
    return render_template('index.html')


@application.route("/home")
def home():
    return render_template('home.html')


@application.route("/about")
def about():
    return render_template('about.html')


@application.route("/services")
def service():
    return render_template('services.html')


@application.route("/contact")
def contact():
    return render_template('contact.html')


@application.route("/career")
def career():
    return render_template('career.html')


@application.route("/blog")
def blog():
    return render_template('blog.html')

@application.route("/payment")
def payment():
    return render_template('payment.html')

@application.route('/success')
def success():
    return render_template('success.html')

@application.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')

        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            buyer_name=name,
            send_email=True,
            email=email,
            redirect_url = "http://localhost:5000/success"
        )


        return redirect(response['payment_request']['longurl'])

    else:
        return redirect("/")



application.run(debug=True)