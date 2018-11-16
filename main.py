from flask import Flask, render_template

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    names = data_manager.get_mentor_names_by_first_name('László')

    return render_template('mentor_names.html', mentor_names=names)


@app.route('/mentor-nicknames-miskolc')
def mentor_nicknames():
    nicknames = data_manager.get_mentor_nickname_miskolc()
    return render_template('mentor_nicknames.html', mentor_names=nicknames)


@app.route('/contact-info-carol')
def contact_of_carol():
    contact_info = data_manager.get_contact_for_carol()
    return render_template('contact_info.html', contact=contact_info)


@app.route('/contact-info-hatowner')
def contact_of_hat_owner():
    contact = data_manager.get_contact_for_hatowner()
    return render_template('contact_info.html', contact=contact)


@app.route('/add-new-applicant')
def add_new_applicant():
    applicant_info = data_manager.add_new_applicant()
    return render_template('applicant_data_page.html', datas=applicant_info)


@app.route('/update-phone-number')
def update_phone_number():
    applicant_info = data_manager.update_phone_number()
    return render_template('applicant_data_page.html', datas=applicant_info)


if __name__ == '__main__':
    app.run(debug=True)
