
# Observer

O Observer Design Pattern lida com relacionamentos um-para-muitos e utiliza eventos para informar as entidades assinadas sobre as alterações em um observável.
O assunto precisa ser monitorado e sempre que houver mudança no assunto, os observadores estão sendo notificados sobre a mudança.
Esse padrão define uma a muitas dependências entre objetos para que um objeto mude de estado, todos os seus dependentes sejam notificados e atualizados automaticamente.

## Quando usar?

> Quando o acoplamento da nossa classe está crescendo, ou quando temos diversas ações diferentes a serem executadas após um determinado processo. Nestes casos, podemos implementar o Observer.

> Ele permite que diversas ações sejam executadas de forma transparente à classe principal, reduzindo o acoplamento entre essas ações, facilitando a manutenção e evolução do código.
