# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Data_ingestion_cleaning_and_creation_of_dimensions_and_fact_tables = Job.from_dict(
    {
        "name": "Data ingestion , cleaning and creation of dimensions and fact tables",
        "tasks": [
            {
                "task_key": "Bronze_stage",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/bronze_stage",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Dimention_date",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/gold-DimDate",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Silver_Sales",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/Silver_Sales",
                    "source": "WORKSPACE",
                },
                "environment_key": "Default",
            },
            {
                "task_key": "Silver_Targets",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/silver_targets",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Silver_product",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/bronze-to-silver-product",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Dimension_product",
                "depends_on": [
                    {
                        "task_key": "Silver_product",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/dim_product",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Silver_region",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/Silver-Region",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Dimension_region",
                "depends_on": [
                    {
                        "task_key": "Silver_region",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/Gold_Region",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Silver_reseller",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/bronze-to-silver-reseller",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Dimention_reseller",
                "depends_on": [
                    {
                        "task_key": "Silver_reseller",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/gold_layer_dim_reseller",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Silver_salesperson",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/silver_salesperson",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Dimention_salesperson",
                "depends_on": [
                    {
                        "task_key": "Silver_salesperson",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/gold-DimSalesperson",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Fact_Sales",
                "depends_on": [
                    {
                        "task_key": "Dimension_region",
                    },
                    {
                        "task_key": "Dimention_salesperson",
                    },
                    {
                        "task_key": "Dimension_product",
                    },
                    {
                        "task_key": "Dimention_reseller",
                    },
                    {
                        "task_key": "Silver_Sales",
                    },
                    {
                        "task_key": "Dimention_date",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/fact_sales",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Fact_Targets",
                "depends_on": [
                    {
                        "task_key": "Dimention_date",
                    },
                    {
                        "task_key": "Dimention_salesperson",
                    },
                    {
                        "task_key": "Silver_Targets",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/gold-FactTargets",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "Silver_salesperson_region",
                "depends_on": [
                    {
                        "task_key": "Bronze_stage",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/anastasiosloukas55@gmail.com/Accenture-Final-Project-Team-3/Silver-Salesperson-Region",
                    "source": "WORKSPACE",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "environments": [
            {
                "environment_key": "Default",
                "spec": {
                    "environment_version": "4",
                },
            },
        ],
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=Data_ingestion_cleaning_and_creation_of_dimensions_and_fact_tables, job_id=649677812501055)
# or create a new job using: w.jobs.create(**Data_ingestion_cleaning_and_creation_of_dimensions_and_fact_tables.as_shallow_dict())
