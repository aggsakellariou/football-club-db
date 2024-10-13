# DBMS Project: Football Club Database System

## Overview

This project focuses on creating a database system to manage an amateur football club's data, including players, teams, matches, and statistics. The project uses **PostgreSQL** to store and manage the data and provides an API for interacting with the database.

## Project Goals

The primary objectives of this project are:
1. Designing and implementing a relational database for managing football club information.
2. Creating SQL queries to retrieve match schedules, player statistics, and team performance.
3. Integrating a Python-based API to run database queries and present results to users.

## Dataset

The data includes information about:
1. **Players**: Contains player records, including name, team, position, goals, and penalties.
2. **Teams**: Stores details about each football team, including their history and performance statistics.
3. **Matches**: Tracks match schedules, scores, and events (goals, penalties, cards).
4. **Match Events**: Logs events like goals, penalties, and cards during each match.

### Database Schema

- **Players** (`id`, `name`, `surname`, `team_id`, `position`, `goals`, `penalties`)
- **Teams** (`id`, `name`, `home_ground`, `history`, `wins`, `losses`, `draws`)
- **Matches** (`id`, `home_team_id`, `away_team_id`, `score_home`, `score_away`, `date`)
- **MatchEvents** (`id`, `match_id`, `event_type`, `player_id`, `time`)
