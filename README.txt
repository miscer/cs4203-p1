# Running the program

If you don't have virtualenv installed, install it:

    $ pip install virtualenv

Create new environment and activate it:

    $ virtualenv -p python3 venv
    $ source venv/bin/activate

Install dependencies:

    $ pip install -r requirements.txt

After that you can run the program:

    $ python -m crypto --help

# Running tests

First make sure the bundler gem is installed:

    $ gem install bundler

Then install the dependencies:

    $ ~/bin/bundle install --path vendor/bundle

Then run the tests:

    $ PYTHONPATH=$(pwd) ~/bin/bundle exec cucumber
