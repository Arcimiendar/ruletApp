(this.webpackJsonprulet_front=this.webpackJsonprulet_front||[]).push([[0],{118:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),l=n(34),i=n.n(l),o=(n(67),n(68),n(29)),c=n(15),s=n(16),m=n(18),u=n(17),d=n(10),p=n(19),h=n(8),f=n(9),E=n.n(f),g=n(5),v=n(13),b=n(120);function y(){var e=Object(h.a)(["\n    mutation {\n        clearAllDepartment {\n            departments{\n                id\n            }\n        }\n    }\n"]);return y=function(){return e},e}var k=E()(y()),C=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={redirect:!1,link:null},n.handleEmployeesLink=n.handleEmployeesLink.bind(Object(d.a)(n)),n.handleHomeLink=n.handleHomeLink.bind(Object(d.a)(n)),n.handleRuletsLink=n.handleRuletsLink.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleEmployeesLink",value:function(e){"/employees_list/"!==window.location.pathname&&this.setState({redirect:!0,link:"/employees_list/"})}},{key:"handleHomeLink",value:function(e){"/"!==window.location.pathname&&this.setState({redirect:!0,link:"/"})}},{key:"handleRuletsLink",value:function(e){"/rulet/list/"!==window.location.pathname&&this.setState({redirect:!0,link:"/rulet/list/"})}},{key:"render",value:function(){return this.state.redirect?r.a.createElement(o.a,{to:this.state.link}):r.a.createElement(g.Navbar,{brand:r.a.createElement("a",null,"The Rulet Application ",this.props.department),alignLinks:"right"},r.a.createElement(g.NavItem,null,r.a.createElement("div",{className:"switch"},r.a.createElement("label",{style:{color:"white"}},"template",r.a.createElement("input",{type:"checkbox",checked:!0,onClick:function(){return window.location.host="127.0.0.1:8000"}}),r.a.createElement("span",{className:"lever"}),"react"))),r.a.createElement(g.NavItem,{onClick:this.handleEmployeesLink},"Employees list"),r.a.createElement(g.NavItem,{onClick:this.handleRuletsLink},"Rulet list"),r.a.createElement(b.a,{mutation:k},(function(e,t){t.data;return r.a.createElement(g.NavItem,{onClick:function(){return e()}},"Clear all departments")})),r.a.createElement(g.NavItem,{onClick:this.handleHomeLink},"Home"))}}]),t}(a.Component);var _=function(){return r.a.createElement("footer",{className:"page-footer",style:{backgroundColor:"#0066ff"}},r.a.createElement("div",{className:"container"},r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col l6 s12"},r.a.createElement("h5",{className:"white-text"},"Information"),r.a.createElement("p",{className:"grey-text text-lighten-4"},"You can use this application to distribute your workers between departments")))),r.a.createElement("div",{className:"footer-copyright",color:"#0066ff"},r.a.createElement("div",{className:"container"},"The Rulet Application 2019")))},O=n(41),j=n(28),N=n.n(j),w=n(7);function S(){var e=Object(h.a)(["\n    mutation ($id: ID!){\n        departmentNotParticipate(id: $id) {\n            department{\n                ruletState\n            }\n        }\n    }\n"]);return S=function(){return e},e}var I=E()(S()),q=function(e){function t(e){var n;Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).socket=null,n.requestModal=null,n.participatingModal=null,n.request=null,n.participating=null,n.department_id=null;var a=new O.a;return n.department_id=a.get("department"),n.socket=new WebSocket((he?"ws://127.0.0.1:8000":"ws://"+window.location.host)+"/ws/notification/"+a.get("department")),n.state={redirect:!1,url:null,not_participate_mutate:!1},n.requestModal=r.a.createElement(g.Modal,{header:"You are requested to participate in the rulet",actions:[r.a.createElement(g.Button,{waves:"green",modal:"close",flat:!0,onClick:function(e){return n.handleAgreeAndParticipate(a.get("department"))}},"Agree and participate"),r.a.createElement(b.a,{mutation:I},(function(e,t){t.data;return r.a.createElement(g.Button,{waves:"green",modal:"close",flat:!0,onClick:function(t){return e({variables:{id:+n.department_id}})}},"Agree and do not participate")})),r.a.createElement(g.Button,{waves:"green",modal:"close",flat:!0},"Disagree, you can agree later")],id:"request"},r.a.createElement("p",null,"You can participate. In that case you will be redirected to the rulet page. ",r.a.createElement("br",null),"Also you can allow rulet and do not participate on it.")),n.participatingModal=r.a.createElement(g.Modal,{header:"You are participating in the rulet",actions:[r.a.createElement(g.Button,{waves:"green",modal:"close",flat:!0},"Ok"),r.a.createElement(g.Button,{waves:"green",modal:"close",flat:!0,onClick:function(e){return n.handleBackToSession(a.get("department"))}},"Back to session")],id:"participating"},r.a.createElement("p",null,"You can go to the rulet session or do it later")),n.socket.onmessage=function(e){if(null===n.request){var t=document.querySelector("#request");n.request=N.a.Modal.init(t)}if(null===n.participating){var a=document.querySelector("#participating");n.participating=N.a.Modal.init(a)}var l=JSON.parse(e.data);if("notification"===l.state){var o=document.querySelector("#message");o&&(o.innerHTML="You need to allow or/and join to the rulet.");var c=document.querySelector("#not_participate");c&&i.a.render(r.a.createElement(w.a,{client:Ee},r.a.createElement(b.a,{mutation:I},(function(e,t){t.data;return r.a.createElement(g.Button,{waves:"light",onClick:function(){e({variables:{id:+n.department_id}}),c.innerHTML="",o&&(o.innerHTML="You are not participating in the rulet, but you still can.")}},"Do not participate in the rulet")}))),c),n.request.open()}else if("participating"===l.state){var s=document.querySelector("#message");s&&(s.innerHTML="You are participating in the rulet.");var m=document.querySelector("#not_participate");m&&(m.innerHTML=""),n.participating.open()}else{var u=document.querySelector("#message");u&&(u.innerHTML="You can begin the rulet session.");var d=document.querySelector("#not_participate");d&&(d.innerHTML="")}},n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleAgreeAndParticipate",value:function(e){this.handleBackToSession(e)}},{key:"handleBackToSession",value:function(e){this.setState({redirect:!0,url:"/rulet/"+e})}},{key:"render",value:function(){return this.state.redirect?r.a.createElement(o.a,{to:this.state.url}):[this.requestModal,this.participatingModal]}},{key:"componentWillUnmount",value:function(){this.socket.close()}}]),t}(a.Component);var L=function(e){var t=new O.a;e.Department&&t.set("department_name",e.Department),e.DepartmentId&&t.set("department",e.DepartmentId);var n=[r.a.createElement(C,{department:t.get("department_name")}),r.a.createElement("main",null,e.children),r.a.createElement(_,null)];return e.avoidNotification||n.push(r.a.createElement(q,null)),n};function B(){var e=Object(h.a)(["\n    query getRuletSessions{\n        departments{\n            id\n            name\n        }\n    }\n"]);return B=function(){return e},e}var x=E()(B());function D(e){var t=e.onChange,n=Object(v.b)(x),a=n.loading,l=n.error,i=n.data;return a?r.a.createElement(L,null,"Loading..."):l?r.a.createElement(L,null,"Error: ",l.message):r.a.createElement(L,null,r.a.createElement("div",{className:"section container"},r.a.createElement(g.Select,{label:"chose department",id:"selected"},i.departments.map((function(e){return r.a.createElement("option",{value:e.id},e.name)}))),r.a.createElement(g.Button,{type:"submit",waves:"light",onClick:function(){var e=document.getElementById("selected");t(e.options[e.selectedIndex].value)}},"Submit",r.a.createElement(g.Icon,{right:!0},"send"))))}var M=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={redirect:!1,department_id:0},n.handleChange=n.handleChange.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleChange",value:function(e){this.setState({redirect:!0,department_id:e})}},{key:"render",value:function(){return this.state.redirect?r.a.createElement(o.a,{to:"/department/"+this.state.department_id}):r.a.createElement(D,{onChange:this.handleChange})}}]),t}(a.Component);function R(){var e=Object(h.a)(["\n    mutation ($id: Int!){\n        clearDepartment(id: $id){\n            department{\n                id\n            }\n        }\n    }\n"]);return R=function(){return e},e}function T(){var e=Object(h.a)(["\n    query ($department_id: Int!){\n        department(id: $department_id){\n            id\n            name\n            description\n            address\n            employees {\n                id\n                firstName\n                lastName\n                image\n            }\n        }\n    }\n"]);return T=function(){return e},e}var A=E()(T()),H=E()(R());function W(e){var t=e.onChange,n=e.departmentId,a=e.onClear,l=e.isEmpty,i=Object(v.b)(A,{variables:{department_id:n}}),o=i.loading,c=i.error,s=i.data;i.refetch;if(o)return r.a.createElement(L,null,"Loading ...");if(c)return r.a.createElement(L,null,"Error: ",c.message);var m=[];s.department.address&&m.push(r.a.createElement(g.CollapsibleItem,{header:"Address",icon:r.a.createElement(g.Icon,null,"place")},s.department.address)),s.department.description.length>0&&m.push(r.a.createElement(g.CollapsibleItem,{header:"Description",icon:r.a.createElement(g.Icon,null,"description")},s.department.description));var u=r.a.createElement(g.CollapsibleItem,{header:"Employees",icon:r.a.createElement(g.Icon,null,"face")},r.a.createElement(g.Collection,null,r.a.createElement(g.CollectionItem,{href:"#",onClick:function(){}},"There is no employees in this department.")));return s.department.employees.length>0?m.push(r.a.createElement(g.CollapsibleItem,{header:"Employees",icon:r.a.createElement(g.Icon,null,"face")},r.a.createElement(g.Collection,null,s.department.employees.map((function(e){return r.a.createElement(g.CollectionItem,{href:"#",onClick:function(){return t("/employee/"+e.id)}},r.a.createElement("img",{src:(he?"http://127.0.0.1:8000":"")+e.image,alt:"",className:"circle",width:"4%",height:"4%"}),e.firstName," ",e.lastName)}))))):m.push(u),r.a.createElement(L,{Department:s.department.name,DepartmentId:s.department.id},r.a.createElement("div",{className:"container"},r.a.createElement("h1",null,s.department.name),r.a.createElement(g.Collapsible,null,l?u:m),r.a.createElement("p",{id:"message"},"You can begin the rulet session."),r.a.createElement(b.a,{mutation:H},(function(e,t){t.data;return r.a.createElement(g.Button,{waves:"light",onClick:function(){e({variables:{id:n}}),a()}},"clear department")}))," ",r.a.createElement("span",null),r.a.createElement(g.Button,{waves:"light",onClick:function(){return t("/rulet/"+n)}},"Participate in the rulet"),r.a.createElement("span",null," "),r.a.createElement("a",{id:"not_participate"}),r.a.createElement("p",null),r.a.createElement("br",null)))}var Y=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={redirect:!1,url:null,empty:!1},n.handleChange=n.handleChange.bind(Object(d.a)(n)),n.handleClear=n.handleClear.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleChange",value:function(e){this.setState({redirect:!0,url:e}),this.forceUpdate()}},{key:"handleClear",value:function(){this.setState({empty:!0})}},{key:"render",value:function(){return this.state.redirect?(this.state.redirect=!1,r.a.createElement(o.a,{to:this.state.url})):r.a.createElement(W,{onChange:this.handleChange,departmentId:this.props.match.params.department_id,isEmpty:this.state.empty,onClear:this.handleClear})}}]),t}(a.Component);function $(){var e=Object(h.a)(["\n    query {\n        employees {\n            id\n            firstName\n            lastName\n            image\n            department {\n                name\n            }\n        }\n    }\n\n"]);return $=function(){return e},e}var P=E()($());function J(e){var t=e.department;return t?". Is in the "+t.name:""}function G(e){var t=e.onChange,n=Object(v.b)(P),a=n.loading,l=n.error,i=n.data;if(a)return r.a.createElement(L,null,"Loading ... ");if(l)return r.a.createElement(L,null," Error: ",l.message);var o=r.a.createElement(g.CollectionItem,{href:"#",onClick:function(){return t(-1)}},"there is no employees yet. Go home.");return i.employees.length>0&&(o=i.employees.map((function(e){return r.a.createElement(g.CollectionItem,{href:"#",onClick:function(){return t(e.id)}},r.a.createElement("img",{src:(he?"http://127.0.0.1:8000":"")+e.image,alt:"",className:"circle",width:"4%",height:"4%"})," ",e.firstName," ",e.lastName,r.a.createElement(J,{department:e.department}))}))),r.a.createElement(L,null,r.a.createElement("div",{className:"section"},r.a.createElement(g.Collection,null,o)))}var U=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={redirect:!1,employee_id:0},n.handleChange=n.handleChange.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleChange",value:function(e){this.setState({redirect:!0,employee_id:e})}},{key:"render",value:function(){return this.state.redirect?this.state.employee_id<0?r.a.createElement(o.a,{to:"/"}):r.a.createElement(o.a,{to:"/employee/"+this.state.employee_id}):r.a.createElement(G,{onChange:this.handleChange})}}]),t}(a.Component);function V(){var e=Object(h.a)(["\n    query ($employee_id: Int!){\n        employee(id: $employee_id) {\n            firstName\n            lastName\n            description\n            dateOfBirth\n            image\n            department {\n                name\n            }\n\n        }\n    }\n"]);return V=function(){return e},e}var z=E()(V());var F=function(e){var t=e.match.params.employee_id,n=Object(v.b)(z,{variables:{employee_id:t}}),a=n.error,l=n.loading,i=n.data;if(l)return r.a.createElement(L,null,"Loading...");if(a)return r.a.createElement(L,null,"ERROR: ",a.message);var o=[];return i.employee.department?o.push(r.a.createElement("a",null,"IS IN THE ",r.a.createElement("b",null,i.employee.department.name))):o.push(r.a.createElement("a",null,r.a.createElement("b",null,"IS NOT IN ANY DEPARTMENT"))),o.push(r.a.createElement("a",null,"WAS BORN IN ",i.employee.dateOfBirth)),r.a.createElement(L,null,r.a.createElement(g.Row,null,r.a.createElement(g.Col,{m:6,s:12},r.a.createElement(g.Card,{className:"blue-grey darken-1",textClassName:"white-text",title:r.a.createElement("span",null,r.a.createElement("img",{src:(he?"http://127.0.0.1:8000":"")+i.employee.image,width:"30%",height:"30%",className:"circle",alt:""}),i.employee.firstName," ",i.employee.lastName),actions:o},i.employee.description))))};function K(){var e=Object(h.a)(["\n    query {\n        ruletSessions {\n            id\n            date\n        }\n    }\n"]);return K=function(){return e},e}var Q=E()(K());function X(e){var t=e.onChange,n=Object(v.b)(Q),a=n.loading,l=n.error,i=n.data;if(a)return r.a.createElement(L,null,"Loading ...");if(l)return r.a.createElement(L,null,"Error: ",l.message);var o=r.a.createElement(g.CollectionItem,{href:"#",onClick:function(){return t(-1)}},"There were no rulet sessions yet. Go home page.");return i.ruletSessions.length>0&&(o=i.ruletSessions.map((function(e){return r.a.createElement(g.CollectionItem,{href:"#",onClick:function(){return t(e.id)}},"rulet session on ",e.date)}))),r.a.createElement(L,null,r.a.createElement("div",{className:"section"},r.a.createElement(g.Collection,null,o)))}var Z=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={redirect:!1,rulet_id:0},n.handleChange=n.handleChange.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleChange",value:function(e){this.setState({redirect:!0,rulet_id:e})}},{key:"render",value:function(){return this.state.redirect?this.state.rulet_id<0?r.a.createElement(o.a,{to:"/"}):r.a.createElement(o.a,{to:"/rulet/list/"+this.state.rulet_id}):r.a.createElement(X,{onChange:this.handleChange})}}]),t}(a.Component);function ee(){var e=Object(h.a)(["\n    query ($rulet_session_id: Int!){\n        ruletSession(id: $rulet_session_id) {\n            active\n            ruletChoices {\n                employee {\n                    id\n                    firstName\n                    lastName\n                    image\n                }\n                department {\n                    name\n                }\n            }\n        }\n    }\n"]);return ee=function(){return e},e}var te=E()(ee());function ne(e){var t=e.onChange,n=e.ruletId,a=Object(v.b)(te,{variables:{rulet_session_id:n}}),l=a.loading,i=a.error,o=a.data;if(l)return r.a.createElement(L,null,"Loading ...");if(i)return r.a.createElement(L,null,"Error: ",i.message);for(var c=[],s=[],m=[],u=o.ruletSession.ruletChoices,d=0;d<u.length;d++)s.includes(u[d].department.name)||(0===c.length&&c.push([]),c[0].push(r.a.createElement("th",null,u[d].department.name)),s.push(u[d].department.name),m[u[d].department.name]=[]),m[u[d].department.name].push(u[d].employee);for(var p=0;p<s.length;p++)m[s[p]].reverse();for(var h=!0;h;){var f=!0;c.push([]);for(var E=0;E<s.length;E++)0!==m[s[E]].length&&f&&(f=!1),0===m[s[E]].length?c[c.length-1].push(r.a.createElement("td",null," ")):function(){var e=m[s[E]].pop();c[c.length-1].push(r.a.createElement("td",{align:"center"},r.a.createElement("a",{onClick:function(){return t(e.id)},href:"#"},r.a.createElement("img",{src:(he?"http://127.0.0.1:8000":"")+e.image,alt:"",className:"circle",height:"4%"})," ",e.firstName," ",e.lastName)))}();f?(h=!1,c.pop()):f=!0}var g="";return o.ruletSession.active&&(g=r.a.createElement("h1",null,"This rulet in session. Results are for now.")),r.a.createElement(L,null,r.a.createElement("div",{className:"container section"},g,r.a.createElement("table",{className:"striped"},c.map((function(e){return r.a.createElement("tr",null,e)})))))}var ae=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={redirect:!1,employee_id:0},n.handleChange=n.handleChange.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleChange",value:function(e){this.setState({redirect:!0,employee_id:e})}},{key:"render",value:function(){return this.state.redirect?r.a.createElement(o.a,{to:"/employee/"+this.state.employee_id}):r.a.createElement(ne,{onChange:this.handleChange,ruletId:this.props.match.params.rulet_id})}}]),t}(a.Component);function re(){var e=Object(h.a)(["\n    query {\n        employeesWithoutDepartment {\n            id\n            lastName\n            firstName\n            dateOfBirth\n            description\n            image\n        }\n    }\n"]);return re=function(){return e},e}var le=E()(re());function ie(e){var t=e.onChange,n=Object(v.b)(le),a=n.error,l=n.loading,i=n.data;return l?r.a.createElement(L,{avoidNotification:!0},"Loading ... "):a?r.a.createElement(L,null,"ERROR: ",a.message):(t(i),r.a.createElement("div",null,"Loading ..."))}var oe=function(e){function t(e){var n;return Object(c.a)(this,t),(n=Object(m.a)(this,Object(u.a)(t).call(this,e))).socket=null,n.socket_is_open=!1,n.modal_message=null,n.state={redirect:!1,url:null,employees_data:null,employees_ready:!1},n.socket=new WebSocket((he?"ws://127.0.0.1:8000":"ws://"+window.location.host)+"/ws/rulet/"+n.props.match.params.department_id),n.socket.onopen=function(e){n.socket_is_open=!0},n.socket.onmessage=function(e){if(null===n.modal_message){var t=document.querySelector("#modal_message");n.modal_message=N.a.Modal.init(t)}var a=JSON.parse(e.data);if("info"===a.state)if(console.log(a.exit),a.exit)n.socket.close(),n.socket_is_open=!1,n.setState({redirect:!0,url:"/department/"+n.props.match.params.department_id});else{var r=document.querySelector("#modal_message_inner");if(!r)return;r.innerHTML=a.info,n.modal_message.open()}else if("chosen"===a.state){for(var l=n.state.employees_data,i={employeesWithoutDepartment:[]},o=0;o<l.employeesWithoutDepartment.length;o++)l.employeesWithoutDepartment[o].id!=a.employee_id&&i.employeesWithoutDepartment.push(l.employeesWithoutDepartment[o]);n.setState({employees_data:i});var c=document.querySelector(".carousel");try{N.a.Carousel.init(c)}catch(s){}}},n.handleChange=n.handleChange.bind(Object(d.a)(n)),n}return Object(p.a)(t,e),Object(s.a)(t,[{key:"handleChange",value:function(e){this.setState({employees_data:e,employees_ready:!0})}},{key:"handleChose",value:function(e){this.socket_is_open&&this.socket.send(JSON.stringify({state:"chosen",employee_id:e}))}},{key:"handleProfilePageRedirect",value:function(e){this.socket.close(),this.socket_is_open=!1,this.setState({redirect:!0,url:"/employee/"+e})}},{key:"handleExit",value:function(){this.socket_is_open&&(this.socket_is_open=!1,this.socket.send(JSON.stringify({state:"exit"})),this.socket.close()),this.setState({redirect:!0,url:"/department/"+this.props.match.params.department_id})}},{key:"render",value:function(){var e=this;return this.state.employees_ready?this.state.redirect?r.a.createElement(o.a,{to:this.state.url}):r.a.createElement(L,{avoidNotification:!0},r.a.createElement("div",{className:"section container"},r.a.createElement("h2",null,"Available employees:"),r.a.createElement(g.Carousel,null,this.state.employees_data.employeesWithoutDepartment.map((function(t){return r.a.createElement("div",{align:"center"},r.a.createElement("p",null),r.a.createElement("img",{src:(he?"http://127.0.0.1:8000":"")+t.image,alt:"",className:"circle"}),r.a.createElement("b",null,t.firstName," ",t.lastName)," ",r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement(g.Button,{waves:"light",onClick:function(n){return e.handleProfilePageRedirect(t.id)}},"show profile")," ",r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement(g.Button,{waves:"light",onClick:function(n){return e.handleChose(t.id)}},"select"))}))),r.a.createElement(g.Button,{waves:"light",floating:!0,large:!0,onClick:function(t){e.modal_message&&e.modal_message.open()},icon:r.a.createElement(g.Icon,null,"message")})," ",r.a.createElement("span",null),r.a.createElement(g.Button,{waves:"light",floating:!0,large:!0,onClick:function(t){return e.handleExit()},icon:r.a.createElement(g.Icon,null,"exit_to_app")})),r.a.createElement(g.Modal,{header:"You received message from server",actions:[r.a.createElement(g.Button,{waves:"green",modal:"close",flat:!0},"Ok")],id:"modal_message"},r.a.createElement("p",{id:"modal_message_inner"},this.state.modal_message))):r.a.createElement(L,{avoidNotification:!0},r.a.createElement(ie,{onChange:this.handleChange}))}}]),t}(a.Component);var ce=function(e){return r.a.createElement(o.d,null,r.a.createElement(o.b,{exact:!0,path:"/",component:M}),r.a.createElement(o.b,{exact:!0,path:"/department/:department_id",component:Y}),r.a.createElement(o.b,{exact:!0,path:"/employees_list/",component:U}),r.a.createElement(o.b,{exact:!0,path:"/employee/:employee_id",component:F}),r.a.createElement(o.b,{exact:!0,path:"/rulet/list/",component:Z}),r.a.createElement(o.b,{exact:!0,path:"/rulet/list/:rulet_id",component:ae}),r.a.createElement(o.b,{exact:!0,path:"/rulet/:department_id",component:oe}))};var se=function(){return[r.a.createElement(ce,null)]};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var me=n(24),ue=n(30),de=n(61),pe=n(60);n.d(t,"DEVELOP",(function(){return he}));var he=!1,fe=new ue.a({link:Object(de.a)({uri:he?"http://127.0.0.1:8000/graphql/":window.location.origin+"/graphql/"}),cache:new pe.a,fetchOptions:{mode:"no-cors"}});i.a.render(r.a.createElement(w.a,{client:fe},r.a.createElement(me.a,null,r.a.createElement(o.b,{component:se}))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}));var Ee=t.default=fe},62:function(e,t,n){e.exports=n(118)},67:function(e,t,n){}},[[62,1,2]]]);
//# sourceMappingURL=main.5ab81383.chunk.js.map