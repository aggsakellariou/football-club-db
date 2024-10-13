import tkinter as tk
import psycopg2

#def for coachname
def coachname():
    try:
        #DB connection
        connection = psycopg2.connect(host="localhost",
                                    port=5432,
                                    database="postgres",
                                    user="postgres",
                                    password="root")
        cursor = connection.cursor()

        #select for 2a
        postgreSQL_select_Query = """
            SELECT t."FIRST_NAME"
            FROM "match" m
            JOIN "player" t ON m."HOME_TEAM_ID" = t."TEAM_ID" OR m."AWAY_TEAM_ID" = t."TEAM_ID"
            WHERE m."MATCH_ID" = 1 AND t."TEAM_ID" = 1 AND t."ACTIVE" = false """

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)

        #print data
        for row in mobile_records:
            result_text.insert(tk.END, "Coach for this match is = {}\n".format(row[0]))

        result_text.configure(state="disabled")

    except (Exception, psycopg2.Error) as error:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error : {}".format(error))
        result_text.configure(state="disabled")

    finally:
        if connection:
            cursor.close()
            connection.close()

#def for goalpenalty
def goalpenalty():
    try:
        #DB connection
        connection = psycopg2.connect(host="localhost",
                                    port=5432,
                                    database="postgres",
                                    user="postgres",
                                    password="root")
        cursor = connection.cursor()

        #select for 2b
        postgreSQL_select_Query = """
            SELECT p."FIRST_NAME" || ' ' || p."LAST_NAME" AS "ΠΑΙΚΤΗΣ", ps."TIME", ps."GOAL", ps."PENALTY"
            FROM public."player_stat" ps
            JOIN public."player" p ON ps."PLAYER_ID" = p."PLAYER_ID"
            WHERE ps."MATCH_ID" = 1 AND (ps."GOAL" IS NOT NULL OR ps."PENALTY" IS NOT NULL); """

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)

        #print data
        for row in mobile_records:
            result_text.insert(tk.END, "Player = {}\n".format(row[0]))
            result_text.insert(tk.END, "Time = {}\n".format(row[1]))
            result_text.insert(tk.END, "Goal = {}\n".format(row[2]))
            result_text.insert(tk.END, "Penalty = {}\n--------------\n".format(row[3]))

        result_text.configure(state="disabled")

    except (Exception, psycopg2.Error) as error:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error : {}".format(error))
        result_text.configure(state="disabled")

    finally:
        if connection:
            cursor.close()
            connection.close()

#def for playerstat
def playerstat():
    try:
        #DB connection
        connection = psycopg2.connect(host="localhost",
                                    port=5432,
                                    database="postgres",
                                    user="postgres",
                                    password="root")
        cursor = connection.cursor()

        #select for 2c
        postgreSQL_select_Query = """
            SELECT
              SUM(ps."GOAL") AS "ΣΥΝΟΛΟ_ΓΚΟΛ",
              SUM(ps."PENALTY") AS "ΣΥΝΟΛΟ_ΠΕΝΑΛΤΙ",
              SUM(ps."YELLOW_CARD") || ' / ' || SUM(ps."RED_CARD") AS "ΚΙΤΡΙΝΕΣ_ΚΑΡΤΕΣ / ΚΟΚΚΙΝΕΣ_ΚΑΡΤΕΣ",
              SUM(ps."MINUTES") AS "ΣΥΝΟΛΟ_ΛΕΠΤΑΑΓΩΝΑ",
              p."POSITION" AS "ΘΕΣΗΠΑΙΚΤΗ"
            FROM public."player_stat" ps
            JOIN public."player" p ON ps."PLAYER_ID" = p."PLAYER_ID"
            WHERE p."PLAYER_ID" = 18
            GROUP BY p."POSITION";"""


        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)

        #print data
        for row in mobile_records:
            result_text.insert(tk.END, "Goal = {}\n".format(row[0]))
            result_text.insert(tk.END, "Penalty = {}\n".format(row[1]))
            result_text.insert(tk.END, "Yellow cards / Red cards = {}\n".format(row[2]))
            result_text.insert(tk.END, "Minutes = {}\n".format(row[3]))
            result_text.insert(tk.END, "Position = {}\n".format(row[4]))

        result_text.configure(state="disabled")

    except (Exception, psycopg2.Error) as error:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error : {}".format(error))
        result_text.configure(state="disabled")

    finally:
        if connection:
            cursor.close()
            connection.close()

#def for teamstat
def teamstat():
    try:
        #DB connection
        connection = psycopg2.connect(host="localhost",
                                        port=5432,
                                        database="postgres",
                                        user="postgres",
                                        password="root")
        cursor = connection.cursor()

        #select for 2d
        postgreSQL_select_Query = """
            SELECT
              COUNT(*) AS "ΣΥΝΟΛΙΚΟΣΑΡΙΘΜΟΣΑΓΩΝΩΝ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΓΗΠΕΔΟΥΧΟΣ",
              SUM(CASE WHEN m."AWAY_TEAM_ID" = 1 THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΦΙΛΟΞΕΝΟΥΜΕΝΗ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 AND m."HOME_SCORE" > m."AWAY_SCORE" THEN 1 WHEN m."AWAY_TEAM_ID" = 1 AND m."AWAY_SCORE" > m."HOME_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΝΙΚΕΣ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 AND m."HOME_SCORE" < m."AWAY_SCORE" THEN 1 WHEN m."AWAY_TEAM_ID" = 1 AND m."AWAY_SCORE" < m."HOME_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΗΤΤΗΜΕΝΕΣ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 AND m."HOME_SCORE" = m."AWAY_SCORE" THEN 1 WHEN m."AWAY_TEAM_ID" = 1 AND m."AWAY_SCORE" = m."HOME_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΙΣΟΠΑΛΙΕΣ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 AND m."HOME_SCORE" > m."AWAY_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΝΙΚΕΣΕΝΤΟΣΕΔΡΑΣ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 AND m."HOME_SCORE" < m."AWAY_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΗΤΤΗΜΕΝΕΣΕΝΤΟΣΕΔΡΑΣ",
              SUM(CASE WHEN m."HOME_TEAM_ID" = 1 AND m."HOME_SCORE" = m."AWAY_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΙΣΟΠΑΛΙΕΣΕΝΤΟΣΕΔΡΑΣ",
              SUM(CASE WHEN m."AWAY_TEAM_ID" = 1 AND m."AWAY_SCORE" > m."HOME_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΝΙΚΕΣΕΚΤΟΣΕΔΡΑΣ",
              SUM(CASE WHEN m."AWAY_TEAM_ID" = 1 AND m."AWAY_SCORE" < m."HOME_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΗΤΤΗΜΕΝΕΣΕΚΤΟΣΕΔΡΑΣ",
              SUM(CASE WHEN m."AWAY_TEAM_ID" = 1 AND m."AWAY_SCORE" = m."HOME_SCORE" THEN 1 ELSE 0 END) AS "ΑΡΙΘΜΟΣΙΣΟΠΑΛΙΕΣΕΚΤΟΣΕΔΡΑΣ"
            FROM public."match" AS m
            WHERE (m."HOME_TEAM_ID" = 1 OR m."AWAY_TEAM_ID" = 1); """

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)

        #print data
        for row in mobile_records:
            result_text.insert(tk.END, "general sum match = {}\n".format(row[0]))
            result_text.insert(tk.END, "Number of homes = {}\n".format(row[1]))
            result_text.insert(tk.END, "Numbers of aways = {}\n".format(row[2]))
            result_text.insert(tk.END, "Number of wins = {}\n".format(row[3]))
            result_text.insert(tk.END, "Number of losses = {}\n".format(row[4]))
            result_text.insert(tk.END, "Number of draws = {}\n".format(row[5]))
            result_text.insert(tk.END, "Number of home wins = {}\n".format(row[6]))
            result_text.insert(tk.END, "Number of home losses = {}\n".format(row[7]))
            result_text.insert(tk.END, "Number of home draws = {}\n".format(row[8]))
            result_text.insert(tk.END, "Number of away wins = {}\n".format(row[9]))
            result_text.insert(tk.END, "Number of away losses = {}\n".format(row[10]))
            result_text.insert(tk.END, "Number of away draws = {}\n".format(row[11]))

        result_text.configure(state="disabled")


    except (Exception, psycopg2.Error) as error:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error : {}".format(error))
        result_text.configure(state="disabled")

    finally:
        if connection:
            cursor.close()
            connection.close()

#window
window = tk.Tk()
window.title("PostgreSQL Data Fetcher")

#buttons's frame
button_frame = tk.Frame(window)
button_frame.pack(side="bottom", pady=10)

#buttons for coachname
fetch_button = tk.Button(button_frame, text="Select 1", command=coachname, padx=10, pady=5)
fetch_button.pack(side="left", padx=5)
#buttons for goalpenalty
fetch_button2 = tk.Button(button_frame, text="Select 2", command=goalpenalty, padx=10, pady=5)
fetch_button2.pack(side="left", padx=5)
#buttons for playerstat
fetch_button3 = tk.Button(button_frame, text="select 3", command=playerstat, padx=10, pady=5)
fetch_button3.pack(side="left", padx=5)
#buttons for teamstat
fetch_button4 = tk.Button(button_frame, text="select 4", command=teamstat, padx=10, pady=5)
fetch_button4.pack(side="left", padx=5)

#text window
result_text = tk.Text(window, height=40, width=100)
result_text.pack()

window.mainloop()
