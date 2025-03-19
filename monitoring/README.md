## Prerequisites

Before diving in, make sure you have the following tools installed:

- `docker`
- `docker-compose` (included with Docker Desktop for Mac and Windows)

## Preparation

All actions should be executed in the repo folder.

If you've already set up your virtual environment using the instruction in the setup, feel free to skip this step.

- **Install Required Packages**:
  Run the following command to install the necessary packages:
  ```bash
  pip install -r requirements.txt
  ```

## Monitoring Example

### Starting Services

To get all required services up and running, execute:

```bash
docker-compose up
```

This will start the following services:

- `db`: PostgreSQL, for storing metrics data
- `adminer`: A handy tool for managing your database
- `grafana`: Your visual dashboarding tool

  **Run the Notebook**:
  Run `baseline_model.py` to download datasets, train the model, and create the reference dashboard.

### Sending Data

To simulate monitoring and send data to the database, run:

```bash
python dummy_metrics.py
```

This script will collect data for a daily batch every 10 seconds, calculate metrics, and insert them into the database. You’ll be able to view these metrics in Grafana on a preconfigured dashboard.

## Accessing the Dashboard

1. Open your browser and go to `http://localhost:3000`.

   - The default username and password are both `admin`.

2. Navigate to the `General/Home` menu and click on `Home`.

3. In the `General` folder, you’ll see an option for `New Dashboard`. Click on it to view the preconfigured dashboard.

You should see the dashboard with all the metrics data.

### Stopping Services

When you're done, stop all services with:

```bash
docker-compose down
```
