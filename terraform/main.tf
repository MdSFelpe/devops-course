terraform {
  required_version = ">= 1.5.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "terraform_test" {
  filename = "${path.module}/terraform-test.txt"
  content  = "Terraform funcionando!"
}