<!DOCTYPE html>
<html>
<head>
<title> {{user}} </title>
<script src='/html/jquery-1.11.0.js'></script>
<script src='/html/app.js'></script>
<style>


#container
{
    width: 50em;
}

#header ul
{
    list-style: none;
    margin: 0;
    padding: 0;
}

#header li
{
    float: left;
    border: 1px solid #bbb;
    border-bottom-width: 0;
    margin: 0;
    width
}

#header a
{

    text-decoration: none;
    display: block;
    background: #eee;
    padding: 0.24em 1em;
    color: #00c;
    width: 8em;
    text-align: center;
}


#header a:hover {
    background: #ddf;
}

#header #selected {
    border-color: black;
}

#header #selected a {
    position: relative;
    top: 1px;
    background: white;
    color: black;
    font-weight: bold;
}

#content {
    border: 1px solid;
    margin: 0px;
    padding: 2em;
    clear: both;
}

#journal {
    border: 1px solid;
    overflow: scroll;
    overflow-x: auto;
}

h1 {
    margin: 0;
    padding: 0 0 1em 0;
}
 
</style> </head> 
<body>

<div id="container">

<div id="header"> 
    <h1> Tabs </h1>
    <ul>
        <li id="selected"><a>Journal</a></li>
        <li><a>Threads</a></li>
        <li><a>Settings</a></li>
    </ul>
    
</div>


<div id="content">

    <div id="journal">
    <h3> Week 42 </h3>
    <div class="el"><span>The</span> The picture above is 250px wide.
     total width of this element is also 250px.</div>
     <div class="el">The picture above is 250px wide.
     The total width of this element is also 250px.</div>
    
     <br>
    
        <form action="list" method="post">
             Item=
             Tag : <input name=tag type="text"/> 
             text  : <input name=value  type="text"/> 
             <input value"Add" type="submit"/>
        </form>
    </div>
</div> 

</div>
</body>
</html>
<!-- vim: set filetype=idl : -->
