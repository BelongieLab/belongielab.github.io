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
{{ member.name }}, {{ member.year }}. {{ member.next }} 
{% endfor %}
  <h4><b>Cornell BS/Masters Alumni & Visitors</b></h4>
  Pragya Verma<br>
  Philip Su<br>
  Andrew Mendez<br>
  Debarun Dhar<br>
  Tomáš Matera<br>
  Bicheng Gao<br>
  Xiaoyan Wu<br>
  Jiaqi Su<br>
  Sam Hoffman<br>
  Dilip Thiagarajan<br>
  Alvin Zhu<br>
  Isay Katsman<br>
  Xi Chen<br>
  Tharun Sankar<br>
  Jeremy Feinstein<br>
  Rohit Jain<br>
  Jonathan Huang<br>
  Arnaud Brejeon<br>
  Jan Jakeš<br>
  Daniel Glasner<br>
  Baoguang Shi<br>
  Chensu Xie<br>
  Yiwei Bai<br>
  Yurong Yu<br>
</div>

<div class="col-sm-6 clearfix">
<h4> <b>UCSD SO(3) PhD Alumni</b> </h4>
{% for member in site.data.so3_alumni %}
{{ member.name }}, {{ member.year }}. {{ member.next }} 
{% endfor %}
  <h4><b>UCSD BS/Masters Alumni & Visitors</b></h4>
  [Grant Van Horn](https://gvanhorn38.github.io/)<br>
  [Phuc X. Nguyen](https://www.linkedin.com/in/phuc-nguyen-60b4a22b/)<br>
  [Andrew Ziegler](https://www.linkedin.com/in/andrewmziegler/)<br>
  [Prasanna Krishnasamy](https://sites.google.com/site/prsnnvk/)<br>
  Nick True<br>
  [Tess Winlock](https://www.linkedin.com/in/twinlock/)<br>
  Fred Birchmore<br>
  [Nadav Ben-Haim](https://www.linkedin.com/in/naydav/)<br>
  [Tom Duerig](http://tomduerig.com/)<br>
  [Louka Dlagnekov](http://vision.ucsd.edu/person/louka-dlagnekov)<br>
  [Diem Vu](https://www.linkedin.com/in/diem-vu-277a49/)<br>
  [Stine Harder](https://www.linkedin.com/in/stine-harder-b1953299/)<br>
  [Chong Cao](http://vision.ucsd.edu/person/chong-cao)<br>
  [Antoni Chan](https://www.cs.cityu.edu.hk/~abchan/)<br>
  [Kyong Mu Lee](https://ee.snu.ac.kr/en/faculty/professor?mode=view&profid=p061)<br>
  [Ana Cristina Murillo](https://sites.google.com/unizar.es/anac)<br>
  [Kris Kitani](http://www.cs.cmu.edu/~kkitani/)<br>
  Tsubasa Yoshida<br>
  [Peter Faymonville](https://www.react.uni-saarland.de/people/faymonville.html)<br>
  Masaaki Kokawa<br>
  Valentin Leonardi<br>
  [Michele Merler](http://www.michelemerler.com/)<br>
  Jocelyn Cambria<br>
  [Robin Hewitt](https://www.linkedin.com/in/robinhewitt/)<br>
  [John Miller](https://www.linkedin.com/in/john-miller-36735b8/)<br>
  [Stephan Steinbach](https://www.linkedin.com/in/stephan-steinbach-84b0044/)<br>
</div>

</div>

