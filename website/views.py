from flask import Blueprint, render_template, redirect, flash, url_for, request, Markup, jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    flash('Military and First Responders recieve a 15% discount', category='success')
    return render_template('home.html')

@views.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@views.errorhandler(404)
@views.route('/gallery', methods=['GET', 'POST'])
def gallery():
    return 'The page you are looking for is currently in development.', 404

@views.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@views.route('/book-a-service', methods=['GET', 'POST'])
def bookservice():
    return render_template('bookservice.html')




service_estimates = {
    "Access Point Installation": "$125",
    "Anti-Virus Installation": "$25",
    "Computer Building": "$400+ *",
    "Computer Cleaning": "$30",
    "Computer Repair": "$250+ *",
    "CPU Cooler Installation": "$60",
    "CPU Installation": "$70",
    "HDD/SSD Installation": "$25",
    "Malware Removal": "$120",
    "OS Installation": "$150",
    "PSU Installation": "$80",
    "RAM Installation": "$25",
    "Router Installation": "$100",
    "Switch Installation": "$120",
    "Wi-Fi Troubleshooting": "$100+ *"
}

@views.route('/price-estimate', methods=['POST'])
def price_estimate():
    selected_service = request.form['service']
    estimate = service_estimates.get(selected_service, "Please select a service.")
    return jsonify(estimate)

@views.route('/price-estimate', methods=['GET', 'POST'])
def estimate():
    return render_template('estimate.html')



@views.route('/services/computer-cleaning', methods=['GET', 'POST'])
def cleaning():
    return render_template('cleaning.html')

@views.route('/services/computer-repair', methods=['GET', 'POST'])
def repair():
    return render_template('repair.html')

@views.route('/services/computer-building', methods=['GET', 'POST'])
def building():
    return render_template('building.html')

@views.route('/services/software-installation', methods=['GET', 'POST'])
def software():
    return render_template('software.html')

@views.route('/services/malware-spyware-removal', methods=['GET', 'POST'])
def malware():
    return render_template('malware.html')

@views.route('/services/operating-system-installation', methods=['GET', 'POST'])
def os():
    return render_template('os.html')

@views.route('/services/hdd-ssd-installation', methods=['GET', 'POST'])
def hdd():
    return render_template('hdd.html')

@views.route('/services/ram-installation', methods=['GET', 'POST'])
def ram():
    return render_template('ram.html')

@views.route('/services/cpu-installation', methods=['GET', 'POST'])
def cpu():
    return render_template('cpu.html')

@views.route('/services/cooler-installation', methods=['GET', 'POST'])
def cooler():
    return render_template('cooler.html')

@views.route('/services/psu-installation', methods=['GET', 'POST'])
def psu():
    return render_template('psu.html')

@views.route('/services/wifi-troubleshooting', methods=['GET', 'POST'])
def wifi():
    return render_template('wifi.html')

@views.route('/services/router-installation', methods=['GET', 'POST'])
def router():
    return render_template('router.html')

@views.route('/services/switch-installation', methods=['GET', 'POST'])
def switch():
    return render_template('switch.html')

@views.route('/services/access-point-installation', methods=['GET', 'POST'])
def access():
    return render_template('access.html')


@views.route('/write-a-review', methods=['GET', 'POST'])
def review():
    return render_template('review.html')


@views.route('/sorry', methods=['GET', 'POST'])
def sorry():
    if request.method == 'GET':
        flash("Sorry, this link isn't working yet...", category='success')
        return redirect(url_for('views.index'))