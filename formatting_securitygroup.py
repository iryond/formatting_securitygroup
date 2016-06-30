#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import json
import csv


if __name__ == "__main__":
    input_file = sys.argv[1]

    f = open(input_file, 'r')
    jsonData = json.load(f)

#    print json.dumps(jsonData,indent = 2)

    for attr in jsonData["SecurityGroups"]:
        SecId = attr["GroupId"]
        GroupName = attr["GroupName"]
        for IpPerm in attr["IpPermissions"]:
            ToPort =  IpPerm.get("ToPort")
            FromPort =  IpPerm.get("FromPort")
            IpProtocol =  IpPerm.get("IpProtocol")
            for Range in IpPerm["IpRanges"]:
                srcIpRanges = Range["CidrIp"]
                print str(SecId)+","+str(GroupName)+","+str(ToPort)+","+str(FromPort)+","+str(IpProtocol)+","+str(srcIpRanges)
            for SecGroup in IpPerm["UserIdGroupPairs"]:
                srcSecID = SecGroup["GroupId"]
                print str(SecId)+","+str(GroupName)+","+str(ToPort)+","+str(FromPort)+","+str(IpProtocol)+","+str(srcSecID)

    f.close()
