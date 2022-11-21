terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = " ~> 3.02"
        }
    }

    required_version = ">= 1.0.0" 
}

provider "azurerm" {
    features {}
}

resource "azurerm_resource_group" "rg-devops-flask-app" {
    name = "DevOps-Projekt-Automated"
    location = "eastus2"
}

resource "azurerm_service_plan" "flask-app-service-plan" {
    name = "plan-dhbw"
    resource_group_name = azurerm_resource_group.rg-devops-flask-app.name
    location = azurerm_resource_group.rg-devops-flask-app.location
    sku_name = "F1"
    os_type = "Linux"
}

resource "azurerm_linux_web_app" "app" {
    name = "website-devops-a"
    resource_group_name = azurerm_resource_group.rg-devops-flask-app.name
    location = "eastus2"
    service_plan_id = azurerm_service_plan.flask-app-service-plan.id
    site_config {
        always_on = false
        application_stack {
            docker_image = "inf20079/dhbw_devops"
            docker_image_tag = "latest"
        }
    }
}