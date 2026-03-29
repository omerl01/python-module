required_packages = ["python3", "pip", "requests", "boto3", "pip"]
print(required_packages)
is_request = "requests" in required_packages

    
is_ansible = "ansible" in required_packages

print(f"is 'request' required? {is_request}")
print(f"is 'ansible' required? {is_ansible}")
required_packages.append("paramiko")
set_required = set(required_packages)
set_required.discard("pip")
print(set_required)

installed_packages = {"docker", "python3", "pip"}
missing_packages = set_required - installed_packages
extra_packages = installed_packages - set_required
common_packages = set_required & installed_packages
print(f"""
      missing: {missing_packages}
      extra: {extra_packages}
      common: {common_packages}
      """
      )
