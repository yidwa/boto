import boto.ec2

access_key = 'AKIAIDTFJCQUW6AW7LDA'
secret_access_key='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'
conn = boto.ec2.connect_to_region("us-west-2", aws_access_key_id = 'AKIAIDTFJCQUW6AW7LDA',
                          aws_secret_access_key= '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')

#conn = EC2Connection(access_key, secret_access_key, region='us-west-2a')
#print(conn)
#   run an instance works
#conn.run_instances('ami-f303fb93', key_name='testingpari',
#                  instance_type='t2.micro', security_groups=['launch-wizard-2'])

# stop instance by instance id
#conn.stop_instances(instance_ids=['i-0d2a74419c255aeb8','i-0ba9cb9c17fc85322'])

# checking running instances
reservations = conn.get_all_reservations()
instances = reservations[0].instances
inst = instances[0]

#print(inst.instance_type)