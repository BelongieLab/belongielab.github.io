---
title: "Belongie Lab - Team"
layout: gridlay
excerpt: "Belongie Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

## Faculty
{% assign number_printed = 0 %}
{% for member in site.data.faculty_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <br>email: <{{ member.email }}></i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Postdoc

<div class="row">

{% for member in site.data.postdoc_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <h5> <a href="{{ member.website }}">Personal website</a> </h5>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

## PhD Students

<div class="row">

{% for member in site.data.phd_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <h5> <a href="{{ member.website }}">Personal website</a> </h5>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

## Research Assistant

<div class="row">

{% for member in site.data.ra_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h4>{{ member.name }}</h4>
  <h5> <a href="{{ member.website }}">Personal website</a> </h5>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

##  Alumni
<div class="row">

<div class="col-sm-6 clearfix">
<h4> <b>Cornell SE(3) PhD Alumni</b> </h4>
{% for member in site.data.se3_alumni %}

{% if member.website == null %}
  {{ member.name }}, {{ member.year }}. {{ member.next }} 

{% else %}
  <a href="{{ member.website }}">{{ member.name }}</a>, {{ member.year }}. {{ member.next }} 

{% endif %}

{% endfor %}
  <h4><b>Cornell BS/Masters Alumni & Visitors</b></h4>
  <a href="https://vision.cornell.edu/se3/people/pragya-verma/">Pragya Verma</a><br>
  <a href="https://www.linkedin.com/in/philipsu522">Philip Su</a><br>
  <a href="https://www.linkedin.com/in/philipsu522">Andrew Mendez</a><br>
  <a href="https://www.linkedin.com/in/debarundhar5">Debarun Dhar</a><br>
  <a href="http://vision.ucsd.edu/person/tomas-matera">Tomáš Matera</a><br>
  <a href="https://www.linkedin.com/in/bicheng-gao-1b719266">Bicheng Gao</a><br>
  <a href="https://www.linkedin.com/in/xiaoyan-wu">Xiaoyan Wu</a><br>
  <a href="https://www.cs.princeton.edu/~jiaqis/personal-website/index.php">Jiaqi Su</a><br>
  <a href="https://www.linkedin.com/in/shoffman5">Sam Hoffman</a><br>
  <a href="https://dthiagarajan.github.io/">Dilip Thiagarajan</a><br>
  <a href="https://www.linkedin.com/in/yzhu1996">Alvin Zhu</a><br>
  <a href="https://isaykatsman.github.io/">Isay Katsman</a><br>
  <a href="https://vision.cornell.edu/se3/people/xi-chen/">Xi Chen</a><br>
  <a href="https://www.linkedin.com/in/tharun-sankar-400501132">Tharun Sankar</a><br>
  <a href="http://jeremyfeinstein.com">Jeremy Feinstein</a><br>
  <a href="https://www.linkedin.com/in/rj288">Rohit Jain</a><br>
  <a href="https://www.linkedin.com/in/gnauhnoj">Jonathan Huang</a><br>
  Arnaud Brejeon<br>
  Jan Jakeš<br>
  <a href="https://sites.google.com/site/dglasner/home">Daniel Glasner</a><br>
  <a href="https://www.microsoft.com/en-us/research/people/bashi/">Baoguang Shi</a><br>
  <a href="http://thomasfuchslab.org/cx">Chensu Xie</a><br>
  <a href="http://thomasfuchslab.org/cx">Yiwei Bai</a><br>
  <a href="https://yurongyou.com/">Yurong Yu</a><br>
</div>

<div class="col-sm-6 clearfix">
<h4> <b>UCSD SO(3) PhD Alumni</b> </h4>
{% for member in site.data.so3_alumni %}
{% if member.website == null %}
  {{ member.name }}, {{ member.year }}. {{ member.next }} 

{% else %}
  <a href="{{ member.website }}">{{ member.name }}</a>, {{ member.year }}. {{ member.next }} 

{% endif %}

{% endfor %}

  <h4><b>UCSD BS/Masters Alumni & Visitors</b></h4>
  <a href="https://gvanhorn38.github.io">Grant Van Horn</a><br>
  <a href="https://www.linkedin.com/in/phuc-nguyen-60b4a22b">Phuc X. Nguyen</a><br>
  <a href="https://www.linkedin.com/in/andrewmziegler">Andrew Ziegler</a><br>
  <a href="https://sites.google.com/site/prsnnvk">Prasanna Krishnasamy</a><br>
  Nick True<br>
  <a href="https://www.linkedin.com/in/twinlock">Tess Winlock</a><br>
  Fred Birchmore<br>
  <a href="https://www.linkedin.com/in/naydav">Nadav Ben-Haim</a><br>
  <a href="http://tomduerig.com">Tom Duerig</a><br>
  <a href="http://vision.ucsd.edu/person/louka-dlagnekov">Louka Dlagnekov</a><br>
  <a href="https://www.linkedin.com/in/diem-vu-277a49">Diem Vu</a><br>
  <a href="https://www.linkedin.com/in/stine-harder-b1953299">Stine Harder</a><br>
  <a href="http://vision.ucsd.edu/person/chong-cao">Chong Cao</a><br>
  <a href="https://www.cs.cityu.edu.hk/~abchan">Antoni Chan</a><br>
  <a href="https://ee.snu.ac.kr/en/faculty/professor?mode=view&profid=p061">Kyong Mu Lee</a><br>
  <a href="https://sites.google.com/unizar.es/anac">Ana Cristina Murillo</a><br>
  <a href="http://www.cs.cmu.edu/~kkitani">Kris Kitani</a><br>
  Tsubasa Yoshida<br>
  <a href="https://www.react.uni-saarland.de/people/faymonville.html">Peter Faymonville</a><br>
  Masaaki Kokawa<br>
  <a href="https://fr.linkedin.com/in/valentin-leonardi-5a6195105">Valentin Leonardi</a><br>
  <a href="http://www.michelemerler.com">Michele Merler</a><br>
  <a href="https://jp.linkedin.com/in/jocelyn-cambria-594812a">Jocelyn Cambria</a><br>
  <a href="https://www.linkedin.com/in/robinhewitt">Robin Hewitt</a><br>
  <a href="https://www.linkedin.com/in/john-miller-36735b8">John Miller</a><br>
  <a href="https://www.linkedin.com/in/stephan-steinbach-84b0044">Stephan Steinbach</a><br>
</div>

</div>

