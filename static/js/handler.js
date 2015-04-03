
<fieldset id="question1">
    <legend>What is the answer to this question?</legend>
    <label><input type="radio" name="q1" value="right"> Right answer</label>
    <label><input type="radio" name="q1" value="wrong"> Wrong answer</label>
</fieldset>
<input type="button" id="answer">
<script type="text/javascript">
    document.getElementById("answer").onclick = validate;
    function validate() {
	    var radios;
	    var i;
	    var right;
	    radios = document.getElementById("question1").getElementsByTagName("input");
 
	    right = false;
	    for(i = 0; i < radios.length; i++) {
		    if(radios[i].value == "yes" && radios[i].checked == true) {
			  right = true;
		    }
	    }
 
	    if(right) {
		    alert("You answered correctly");
	    } else {
		    alert("Wrong answer");
	    }
    }
</script>