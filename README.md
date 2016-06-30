# formatting_securitygroup
format securitygroup json(from aws cli) to csv

# how to use
\# aws ec2 describe-security-groups --region=ap-northeast-1 > json;python2.7 security_group.py json
