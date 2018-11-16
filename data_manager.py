import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_names(cursor):
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nickname_miskolc(cursor):
    cursor.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    nicknames = cursor.fetchall()
    return nicknames


@database_common.connection_handler
def get_contact_for_carol(cursor):
    cursor.execute("""SELECT first_name, last_name, phone_number FROM applicants WHERE first_name='Carol';""")
    contact_info = cursor.fetchall()
    return contact_info


@database_common.connection_handler
def get_contact_for_hatowner(cursor):
    cursor.execute("""SELECT first_name, last_name, phone_number FROM applicants 
                    WHERE email LIKE '%@adipiscingenimmi.edu';""")
    hat_contact_info = cursor.fetchall()
    return hat_contact_info


@database_common.connection_handler
def add_new_applicant(cursor):
    cursor.execute("""INSERT INTO applicants(first_name, last_name, phone_number, email, application_code) 
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');
                    SELECT first_name, last_name, phone_number, email, application_code FROM applicants 
                    WHERE last_name='Schaffarzyk';""")
    new_applicant = cursor.fetchall()
    return new_applicant


@database_common.connection_handler
def update_phone_number(cursor):
    cursor.execute("""SELECT first_name, last_name, phone_number, email, application_code FROM applicants 
                    WHERE first_name='Jemima' AND last_name='Foreman';
                    UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman';
                    SELECT first_name, last_name, phone_number, email, application_code FROM applicants 
                    WHERE first_name='Jemima' AND last_name='Foreman';""")
    updated_phone_number = cursor.fetchall()
    return updated_phone_number


@database_common.connection_handler
def remove_applicants(cursor):
    cursor.execute(""" """)
    removed_applicants = cursor.fetchall()
    return removed_applicants
