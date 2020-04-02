# 						maven


#####  1.maven的作用
	
	i.增加第三方Jar   (commons-fileupload.jar   commons-io.jar)
	ii.jar包之间的依赖关系 （commons-fileupload.jar 自动关联下载所有依赖的Jar，并且不会冲突）

b.将项目拆分成若干个模块

##### 2.Maven概念：
	是一个基于Java平台的 自动化构建工具
	make-ant-maven-gradle

清理：删除编译的结果，为重新编译做准备。
编译：java->class
测试： 针对于 项目中的关键点进行测试，亦可用 项目中的测试代码 去测试开发代码；
报告：将测试的结果 进行显示
打包： 将项目中包含的多个文件 压缩成一个文件， 用于安装或部署。 （java项目-jar、web项目-war）
安装：将打成的包  放到  本地仓库，供其他项目使用。
部署：将打成的包  放到  服务器上准备运行。
	--将java、js、jsp等各个文件 进行筛选、组装，变成一个 可以直接运行的项目
	-- 大米->米饭


	-Eclipse中部署的web项目可以运行
	-将Eclipse中的项目，复制到tomcat/webapps中则不能运行
	-项目可以在webappas中直接运行
	
	Eclipse中的项目 ，在部署时 会生成一个 对应的 部署项目(在wtpwebapps中)，区别在于： 
	部署项目 没有源码文件src(java)，只有编译后的class文件和jsp文件
	因为二者目录结构不一致，因此tomcat中无法直接运行 Eclips中复制过来的项目 
	（因为 如果要在tomcat中运行一个项目，则该项目 必须严格遵循tomcat的目录结构）
	
	Eclipse中的项目 要在tomcat中运行，就需要部署： a.通过Eclipse中Add and Remove按钮进行部署
						      b.将Web项目打成一个war包，然后将该war包复制到tomcat/webapps中 即可执行运行



 自动化构建工具maven：将 原材料（java、js、css、html、图片）->产品（可发布项目）


 编译-打包-部署-测试   --> 自动构建


##### 下载配置maven
	a.配置JAVA_HOME
	b.配置MAVEN_HOME    :    D:\apache-maven-3.5.3\bin
	      M2_HOME
	c.配置path
		%MAVEN_HOME%\bin	
	d.验证
		mvn -v
	e.配置本地仓库  maven目录/conf/settings.xml
		默认本地仓库 ：C:/Users/YANQUN/.m2/repository
		修改本地仓库：  <localRepository>D:/mvnrep</localRepository>

##### 使用maven
	约定 优于 配置 

	硬编码方式：job.setPath("d:\\abc") ;
	配置方式：
		job
	conf.xml                   <path>d:\\abc</path>

	约定：使用默认值d:\\abc
		job


	maven约定的目录结构：
		项目
		-src				
			--main			：程序功能代码
				--java		 java代码  (Hello xxx)
				--resources      资源代码、配置代码
			--test			：测试代码
				--java			
				--resources	
	        pom.xml
		
	<groupId>域名翻转.大项目名</groupId>
	<groupId>org.lanqiao.maven</groupId>

	<artifactId>子模块名</artifactId>
	<artifactId>HelloWorld</artifactId>


	<version>版本号</version>
	<version>0.0.1-SNAPSHOT</version>




##### 依赖：
commons-fileupload.jar --> commons-io.jar
A中的某些类 需要使用B中的某些类，则称为A依赖于B
在maven项目中，如果要使用 一个当时存在的Jar或模块，则可以通过 依赖实现（去本地仓库、中央仓库 
, 远程仓库去寻找）去寻找）


 ##### 执行mvn：  必须在pom.xml所在目录中执行
 
maven常见命令： （第一次执行命令时，因为需要下载执行该命令的基础环境，

所以会从中央仓库下载该环境到本地仓库）
编译：  (  Maven基础组件 ，基础Jar)
mvn compile   --只编译main目录中的java文件
mvn test     测试
mvn package          打成jar/war
mvn install  将开发的模块 放入本地仓库，供其他模块使用 （放入的位置 是通过gav决定）

mvn clean  删除target目录（删除编译文件的目录）
运行mvn命令，必须在pom.xml文件所在目录

私服 : 

本地仓库 ----私服-----中央仓库去寻找


普通项目:jar
Web项目: War


配置本地仓库 settings

打包方式：
java工程——jar
web项目-war
父工程-pom


继承实现步骤：
1.建立父工程： 父工程的打包方式为pom 

2.在父工程的pom.xml中编写依赖：
<dependencyManagement>
  	<dependencies>
  		<dependency>


3.子类:
  <!-- 给当前工程 继承一个父工程：1加入父工程坐标gav   2当前工程的Pom.xml到父工程的Pom.xml之间的 相对路径  -->
 	 <parent>
 	 	<!-- 1加入父工程坐标gav -->
 	 	  <groupId>org.lanqiao.maven</groupId>
		  <artifactId>B</artifactId>
		  <version>0.0.1-SNAPSHOT</version>
		 <!-- 2当前工程的Pom.xml到父工程的Pom.xml之间的 相对路径 --> 
		  <relativePath>../B/pom.xml</relativePath>
 	 </parent>


4.在子类中 需要声明 ：使用那些父类的依赖

 			 <dependency>
	  		  <!-- 声明：需要使用到父类的junit （只需要ga） -->
				<groupId>junit</groupId>
				<artifactId>junit</artifactId>
			  </dependency>
	  	

聚合：

Maven项目能够识别的： 自身包含、本地仓库中的

Maven2依赖于Maven1，则在执行时：必须先将Maven1加入到本地仓库(install)，之后才能执行Maven2
以上 前置工程的install操作，可以交由“聚合” 一次性搞定。。。


聚合的使用：

在一个总工程中配置聚合： （聚合的配置 只能配置在（打包方式为pom）的Maven工程中）
modules
  <modules>
  		<!--项目的根路径  -->
  	  <module>../Maven1</module>
  	  <module>../Maven2</module>
  	  
  </modules>
配置完聚合之后，以后只要操作总工程，则会自动操作 改聚合中配置过的工程

注意：clean命令 是删除 target目录，并不是清理install存放入的本地仓库


聚合：
	Maven将一个大工程拆分成 若干个子工程（子模块） 
	聚合可以将拆分的多个子工程 合起来
继承：
	父->子工程,可以通过父工程  统一管理依赖的版本

部署Web工程：war

通过maven直接部署运行web项目：
a.配置cargo
b. maven命令：deploy

实际开发中，开发人员 将自己的项目开发完毕后  打成war包(package) 交给实施人员去部署；


http://www.mvnrepository.com









依赖：
A jar -> B jar
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.0</version>
			<scope>test</scope>
		</dependency>


依赖
1.依赖的范围、依赖的有效性
	compile(默认)  test  provided
2.依赖排除
   A.jar ->B.jar
  当我们通过maven引入A.jar时，会自动引入B.jar
	A.jar(x.java ,y.java,z.java)     B.jar(p.java  c.java  i.java)
		A.jar和B.jar之间的 依赖的本质：z.java ->c.java

   <!-- 排除依赖 beans -->
		    <exclusions>
		    	<exclusion>
		    		<groupId>org.springframework</groupId>
   					 <artifactId>spring-beans</artifactId>
		    	</exclusion>
		    
		    </exclusions>
	
依赖：
 a.commons-fileupload.jar  commons-io.jar  :虽然我们实际开发时，认为二者jar必须关联，
 但是maven可能不这么认为。
 b.如果X.jar 依赖于Y.jar，但是在引入X.jar之前  已经存在了Y.jar，则maven不会再在 引入X.jar时 引入Y.jar
 
3.依赖的传递性
A.jar-B.jar->C.jar

要使 A.jar ->C.jar:当且仅当 B.jar 依赖于C.jar的范围是compile

多个maven项目（模块）之间如何 依赖： p项目 依赖于->q项目
1.  p项目 install 到本地仓库
2.  q项目 依赖：
		<!-- 本项目  依赖于HelloWorld2项目 -->
 		 <dependency>
 		 	 <groupId>org.lanqiao.maven</groupId>
			  <artifactId>HelloWorld2</artifactId>
			  <version>0.0.1-SNAPSHOT</version>
			  <scope>compile</scope 
 		 </dependency>


在Eclipse中创建maven工程：
1.配置maven:
配置maven版本
配置本地仓库  ：  设置settings.xml

在eclipse中编写完pom.xml依赖后，需要maven-update project

package:
resources
compile
test
package

maven生命周期:
生命周期和构建的关系：
生命周期中的顺序：a b c d e 
当我们执行c命令，则实际执行的是 a b c 
该命令执行之前的所有命令

生命周期包含的阶段：3个阶段
clean lifecycle ：清理
	pre-clean  clean  post-clearn

default lifecycle ：默认(常用)
	

site lifecycle：站点
	pre-site   site   post-site site-deploy

再次强调：在pom.xml中增加完依赖后 需要maven - update project


约定大于配置




 
3.依赖的传递性

A.jar-B.jar->C.jar

要使 A.jar ->C.jar :当且仅当 B.jar 依赖于C.jar的范围是compile


HelloWorldTime ->HelloWorld2 ->junit

4依赖原则：为了防止冲突
a.路径最短优先原则
b.路径长度相同：
	i.在同一个pom.xml文件中有2个相同的依赖（覆盖）：后面声明的依赖 会覆盖前面声明的依赖 （严禁使用本情况，严禁在同一个pom中声明2个版本不同的依赖）
	ii.如果是不同的 pom.xml中有2个相同的依赖（优先）：则先声明的依赖 ，会覆盖后声明的依赖


（JDK只能够识别 source folder中的源码）


多个maven项目（模块）之间如何 依赖： p项目 依赖于->q项目
1.  p项目 install 到本地仓库
2.  q项目 依赖：
		<!-- 本项目  依赖于HelloWorld2项目 -->
 		 <dependency>
 		 	 <groupId>org.lanqiao.maven</groupId>
			  <artifactId>HelloWorld2</artifactId>
			  <version>0.0.1-SNAPSHOT</version>
 		 </dependency>


default lifecycle ：默认(常用)
	

site lifecycle：站点
	pre-site   site   post-site site-deploy

再次强调：在pom.xml中增加完依赖后 需要maven - update project




统一项目的jdk：
build path:删除旧版本，增加新版本
右键项目-属性-Project Factors -java version 改版本  （之前存在要改的版本）

通过maven统一jdk版本：
   <profiles>
    <profile>  
        <id>jdk-18</id>  
        <activation>  
            <activeByDefault>true</activeByDefault>  
            <jdk>1.8</jdk>  
        </activation>  
        <properties>  
            <maven.compiler.source>1.8</maven.compiler.source>  
            <maven.compiler.target>1.8</maven.compiler.target>  
            <maven.compiler.compilerVersion>1.8</maven.compiler.compilerVersion>  
        </properties>   
    </profile>  
 </profiles>
