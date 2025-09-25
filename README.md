# CS-454-554-Project1
A simple cloud pounds-to-kilograms conversion service on an AWS EC2 instance using Python Flask.

# Pounds → Kilograms REST API (Flask on AWS EC2)

A REST web service that converts pounds (lbs) to kilograms (kg).

## Public Endpoint
- Base URL: http://18.223.16.96
- Endpoint: GET /convert?lbs=<number>

### Example Response (200)
json
{
  "lbs": 150.0,
  "kg": 68.039,
  "formula": "kg = lbs * 0.45359237"
}

# 1. SSH into instance
ssh -i cc-ec2-key.pem ec2-user@18.223.16.96

# 2. Install Python, pip, git, nginx
sudo yum update -y
sudo yum install -y python3 python3-pip git nginx

# 3. Clone repo
git clone https://github.com/HaloX627/CS-454-554-Project1.git
cd CS-454-554-Project1

# 4. Install dependencies
pip3 install --user -r requirements.txt

# 5. Configure systemd
sudo cp deploy/pl.service /etc/systemd/system/pl.service
sudo systemctl daemon-reload
sudo systemctl enable --now pl

# 6. Configure NGINX
sudo cp deploy/nginx.conf.example /etc/nginx/nginx.conf
sudo nginx -t
sudo systemctl enable --now nginx
sudo systemctl restart nginx

# Termination
- To stop or terminate the EC2 instance, go to the EC2 console.
  From the instance state dropdown menu, select stop or terminate.
  Stop will essentailly pause the instance and can be restarted later.
  Terminate will remove it entirely.
- For EBS Volumes, got to Volumes from the EC2 console.
  Select any volume with State = active.
  Under Actions, select Delete Volume.
- For Key Pairs, they can also be deleted from the EC2 console.
