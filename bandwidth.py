# network environment
maxbandwidthinMbps = 1000
numberofusers = 200

# applications
app1usageinbps = 200000
app2usageinbps = 100000
newappusageinbps = 350000

# calculating current network capacity in Bps
bandwidthinbps = maxbandwidthinMbps * 1000000

# calculating usage in Bps
usageinbps = (app1usageinbps + app2usageinbps) * numberofusers

# calculating current availability in Bps
availabilityinbps = bandwidthinbps - usageinbps

# calculating availability after installing new app
availabilityafternewappinbps = availabilityinbps - (newappusageinbps * numberofusers)
availabilityafternewappinMbps = (availabilityafternewappinbps / 1000000)

# printing results
print(f"""
Network capacity is: {str(bandwidthinbps)} bps.
Current usage is: {str(usageinbps)} bps across {str(numberofusers)} users.
Availability is: {str(availabilityinbps)} bps.
New application requires: {str(newappusageinbps * numberofusers)} bps across {str(numberofusers)} users.
Bandwidth available after new application install: {str(availabilityafternewappinMbps)} Mbps.
""")

if (availabilityafternewappinMbps < 0):
    print("Not enough bandwidth!")
