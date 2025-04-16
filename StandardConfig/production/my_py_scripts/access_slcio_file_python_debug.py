import os
import sys


def read_slicio_files(file_names):
    for file_name in file_names:
        print(f"Reading file: {file_name}")
        # Open the SLCIO file
        reader = pyLCIO.IOIMPL.LCFactory.getInstance().createLCReader()
        try:
            reader.open(file_name)
            # Loop over all events in the file
            while True:
                event = reader.readNextEvent()
                if not event:
                    break
                print("Reading event", event.getEventNumber())

                import time

                from IPython import embed

                embed()
                time.sleep(1)
                # Process your event data here
                # For example, access some particle data:
                # collection = event.getCollection('MCParticle')
                # for particle in collection:
                #     print(particle.getEnergy())

        except Exception as e:
            print(f"Error reading {file_name}: {e}")
        finally:
            reader.close()


if __name__ == "__main__":
    file_names = ["debugTPC_v02_REC.slcio", "debugTPC10events_v11_REC.slcio"]
    read_slicio_files(file_names)
