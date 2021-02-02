import backend_testing
import frontend_testing
import db_connector
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test", default="combined", help="Which test to run")
args = parser.parse_args()


def combined_test(id, name):
    try:
        # Run the tests
        backend_testing.post(id, name)
        id = db_connector.get_ids()
        backend_testing.get(id)
        db_connector.get_table()
        if name == frontend_testing.frontend_test(id):
            print("Test succeeded")
        else:
            raise Exception
        # Delete the new users to not spam the DB
        db_connector.delete_user(id)
    except:
        print("Test failed")


if args.test == "combined":
    combined_test(3, "Posted user1")
elif args.test == "backend":
    backend_testing.post(3, "Posted user1")
    id = db_connector.get_ids()
    backend_testing.get(id)
elif args.test == "frontend":
    frontend_testing.frontend_test(1)