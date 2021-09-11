# Introdução ao SQL
# Capítulo 09 - Design de Banco de Dados


# Libraries

import sqlite3


# Program

Filename = "SurgeTechDB.db"

conn = sqlite3.connect(Filename)
curs = conn.cursor()


company = """ CREATE TABLE company (
              company_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name VARCHAR(30) NOT NULL,
              description VARCHAR(60),
              primary_contact_id INTEGER NOT NULL );
          """


room = """CREATE TABLE room (
          room_id INTEGER PRIMARY KEY AUTOINCREMENT,
          floor_number INTEGER NOT NULL,
          seat_capacity INTEGER NOT NULL );
       """


presentation = """CREATE TABLE presentation (
                  presentation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  booked_company_id INTEGER NOT NULL,
                  booked_room_id INTEGER NOT NULL,
                  start_time TIME,
                  end_time TIME );
               """


attendee = """CREATE TABLE attendee (
              attendee_id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name VARCHAR(30) NOT NULL,
              last_name VARCHAR(30) NOT NULL,
              phone CARCHAR(30),
              email VARCHAR(30),
              vip BOOLEAN DEFAULT(0) );
           """


presentation_atendance = """CREATE TABLE presentation_atendance (
                            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            presentation_id INTEGER,
                            attendee_id INTEGER );
                         """


# Creating Tables

curs.execute(company)
curs.execute(room)
curs.execute(presentation)
curs.execute(attendee)
curs.execute(presentation_atendance)


print("ALL tables created")

    
# Closing

curs.close()
conn.close()
print("")




