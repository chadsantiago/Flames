from flames import app
from flask import Flask, render_template, url_for, request, redirect
from flames.duplicate import remove_duplicate
from flames.forms import NameForm


@app.route('/', methods=['POST', 'GET'])
def home():
    form = NameForm(request.form)

    if request.method == 'POST' and form.validate():

        # pass the class of the inputs
        name1 = request.form['firstname'] 
        name2 = request.form['secondname']

        # convert names into lower case 
        name1 = name1.lower()
        name2 = name2.lower()

        name_one = name1
        name_two = name2

        # delete spaces 
        name1 = name1.replace(" ", "")
        name2 = name2.replace(" ", "")

        # convert names into list
        name1_list = list(name1)
        name2_list = list(name2)

        proceed = True
        while proceed:

            # call function
            ret_list = remove_duplicate(name1_list, name2_list)

            # take out concatenated list 
            con_list = ret_list[0]

            # take out flag value from return list 
            proceed = ret_list[1]

            # find the index of *
            start_index = con_list.index("*")

            # all characters before * store in name1_list
            name1_list = con_list[: start_index]

            # all characters before * store in name2_list
            name2_list = con_list[start_index + 1:]


        # count remaining characters
        count = len(name1_list) + len(name2_list)

        # FLAMES acronym
        status = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        # loop until one item in result remains
        while len(status) > 1:

            # value to be slice
            split_index = (count % len(status) - 1)

            if split_index >= 0:

                # start slicing
                right = status[split_index + 1:]
                left = status[: split_index]

                # concatenate list
                status = right + left

            else:
                status = status[: len(status) - 1]
        
        # final result 
        result = status[0]
        return redirect(url_for('relationship', name_one=name_one, name_two=name_two, result=result))

    return render_template('index.html', form=form)


@app.route('/relationship')
def relationship():
    result = request.args.get('result', None) # get result from the url
    # get names from the url
    name1 = request.args.get('name_one', None)
    name2 = request.args.get('name_two', None)

    name1 = name1.upper()
    name2 = name2.upper()

    if result == "Friendship" :

        status = f"{name1} and {name2} are FRIENDS!"

    elif result == "Love":

        status = f"{name1} and {name2} are LOVERS!"

    elif result == "Affection":

        status = f"{name1} is attracted to {name2}!"

    elif result == "Marriage":

        status = f"{name1} and {name2} are MARRIED!"

    elif result == "Enemy":

        status = f"{name1} and {name2} are sworn ENEMIES!"

    elif result == "Siblings":

        status = f"{name1} and {name2} are SIBLINGS!"

    else :

        msg = "error"

    return render_template('result.html', status=status)