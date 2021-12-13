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
<h4> <b>SE(3) Alumni @ Cornell</b> </h4>
{% for member in site.data.se3_alumni %}
{{ member.name }}, Graduation year: {{ member.year }}, Next step: {{ member.next }} 
{% endfor %}
</div>

<div class="col-sm-6 clearfix">
<h4> <b>SO(3) Alumni @ UCSD</b> </h4>
{% for member in site.data.so3_alumni %}
{{ member.name }}, Graduation year: {{ member.year }}, Next step: {{ member.next }} 
{% endfor %}
</div>

</div>

