package com.example.finalexam;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class login extends AppCompatActivity {
    TextView nickT, idT, emailT;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();

        nickT = findViewById(R.id.nickInfo);
        idT = findViewById(R.id.idInfo);
        emailT = findViewById(R.id.emailInfo);

        Button logout = findViewById(R.id.logout);

        Intent getintent = getIntent();

        nickT.setText(getintent.getExtras().get("nick").toString());
        idT.setText(getintent.getExtras().get("id").toString());
        emailT.setText(getintent.getExtras().get("email").toString());

        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(login.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}