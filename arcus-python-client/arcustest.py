from arcus import *
from arcus_mc_node import ArcusMCNodeAllocator
from arcus_mc_node import EflagFilter
import datetime, time, sys

def main():
    client = Arcus(ArcusLocator(ArcusMCNodeAllocator(ArcusTranscoder())))

    # Usage: python3 arcustest.py 172.17.0.3~5 arcprime-cloud
    client.connect(sys.argv[1], sys.argv[2])

    print ("\n########## Connection Success! ##########")

    timeout = 20

    # Key-Value register.
    client.set('20120001', 'A', timeout)
    client.set('20120002', 'B', timeout)
    client.set('20120003', 'C', timeout)
    client.set('20120004', 'D', timeout)
    client.set('20120005', 'E', timeout)

    start_time = time.time()
    
    # Get value by Keys.
    client.get('20120001')
    client.get('20120002')
    client.get('20120003')
    client.get('20120004')
    client.get('20120005')

    end_time = time.time()

    print ("########## Arcus Running Time ##########")
    print (end_time - start_time)
    print ("")

    client.disconnect()
    return

if __name__ == "__main__":
    main()
